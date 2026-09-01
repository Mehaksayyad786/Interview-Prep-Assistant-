import React, { useState, useEffect, useRef } from "react";
import { useNavigate } from "react-router-dom";
import { MessageSquare, Send, CheckCircle2, ChevronRight, HelpCircle } from "lucide-react";

export const Interview: React.FC = () => {
  const navigate = useNavigate();
  const [interviewId, setInterviewId] = useState<string | null>(null);

  // Live session states
  const [questionNum, setQuestionNum] = useState<number>(1);
  const [questionText, setQuestionText] = useState<string>("");
  const [questionType, setQuestionType] = useState<string>("descriptive");
  const [options, setOptions] = useState<string[]>([]);
  const [answer, setAnswer] = useState<string>("");
  const [isCompletedState, setIsCompletedState] = useState<boolean>(false);

  // Loading/submission states
  const [loading, setLoading] = useState<boolean>(true);
  const [submitting, setSubmitting] = useState<boolean>(false);
  const [completing, setCompleting] = useState<boolean>(false);
  const [error, setError] = useState<string | null>(null);

  // Reference to scroll text area
  const textareaRef = useRef<HTMLTextAreaElement>(null);

  useEffect(() => {
    const id = localStorage.getItem("current_interview_id");
    if (!id) {
      navigate("/setup");
      return;
    }
    setInterviewId(id);
    fetchQuestion(id);
  }, []);

  const fetchQuestion = async (id: string) => {
    setLoading(true);
    setError(null);
    const token = localStorage.getItem("token");

    try {
      const response = await fetch(`http://127.0.0.1:8000/api/interview/question/${id}`, {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });

      const data = await response.json();

      if (response.ok) {
        setIsCompletedState(data.is_completed);
        setQuestionNum(data.question_number);
        setQuestionText(data.question);
        setQuestionType(data.type || "descriptive");
        setOptions(data.options || []);
        setAnswer(""); // Reset answer input on new question
      } else {
        setError(data.detail || "Failed to load interview question.");
      }
    } catch (err) {
      setError("Failed to retrieve question. Check backend connectivity.");
    } finally {
      setLoading(false);
    }
  };

  const handleSubmitAnswer = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!answer.trim() || submitting || !interviewId) return;

    setSubmitting(true);
    setError(null);
    const token = localStorage.getItem("token");

    try {
      const response = await fetch(`http://127.0.0.1:8000/api/interview/answer/${interviewId}`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${token}`,
        },
        body: JSON.stringify({
          question_number: questionNum,
          answer: answer.trim(),
        }),
      });

      const data = await response.json();

      if (response.ok) {
        setAnswer("");
        await fetchQuestion(interviewId);
      } else {
        setError(data.detail || "Failed to submit answer. Please try again.");
      }
    } catch (err) {
      setError("Network error occurred during submission.");
    } finally {
      setSubmitting(false);
    }
  };

  const handleCompleteInterview = async () => {
    if (!interviewId || completing) return;

    setCompleting(true);
    setError(null);
    const token = localStorage.getItem("token");

    try {
      const response = await fetch(`http://127.0.0.1:8000/api/interview/complete/${interviewId}`, {
        method: "POST",
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });

      const data = await response.json();

      if (response.ok) {
        localStorage.removeItem("current_interview_id");
        navigate(`/results/${interviewId}`);
      } else {
        setError(data.detail || "Failed to process interview results.");
      }
    } catch (err) {
      setError("Failed to generate results summary. Check network connection.");
    } finally {
      setCompleting(false);
    }
  };

  const wordCount = answer.trim() ? answer.trim().split(/\s+/).length : 0;

  return (
    <div className="mx-auto max-w-4xl px-4 py-8 sm:px-6 lg:px-8 min-h-[calc(100vh-4rem)] flex flex-col justify-center">
      {/* Session Progress */}
      <div className="mb-6 space-y-2">
        <div className="flex justify-between text-xs font-semibold text-slate-600 dark:text-slate-400">
          <span>Mock Interview Session</span>
          <span>{isCompletedState ? "Finished" : `Question ${questionNum} of 20`}</span>
        </div>
        <div className="h-2 w-full rounded-full bg-slate-200 dark:bg-slate-900 overflow-hidden border border-slate-300 dark:border-slate-800">
          <div
            className="h-full bg-gradient-to-r from-indigo-500 via-purple-500 to-pink-500 transition-all duration-500"
            style={{ width: `${isCompletedState ? 100 : ((questionNum - 1) / 20) * 100}%` }}
          />
        </div>
      </div>

      {error && (
        <div className="mb-6 rounded-lg border border-red-500/30 bg-red-500/10 p-4 text-sm text-red-500 dark:text-red-400">
          {error}
        </div>
      )}

      {/* Main card */}
      <div className="rounded-2xl border border-slate-200 bg-white p-6 md:p-8 shadow-sm dark:border-slate-800 dark:bg-slate-900/60 dark:shadow-xl backdrop-blur-xl flex-1 flex flex-col justify-between min-h-[400px]">
        {loading ? (
          <div className="flex-1 flex flex-col items-center justify-center space-y-4 py-12">
            <div className="relative flex h-12 w-12 items-center justify-center rounded-xl bg-indigo-600/10 text-indigo-500">
              <MessageSquare className="h-6 w-6 animate-pulse" />
              <div className="absolute inset-0 animate-ping rounded-xl bg-indigo-600/20" />
            </div>
            <p className="text-sm font-medium text-slate-600 dark:text-slate-400 animate-pulse">
              AI is formulating your next question...
            </p>
          </div>
        ) : isCompletedState ? (
          <div className="flex-1 flex flex-col items-center justify-center text-center space-y-6 py-12 max-w-lg mx-auto">
            <div className="flex h-16 w-16 items-center justify-center rounded-full bg-green-500/10 text-green-500 shadow-inner">
              <CheckCircle2 className="h-10 w-10 animate-bounce" />
            </div>
            <div>
              <h2 className="text-2xl font-bold text-slate-900 dark:text-white">All Questions Completed!</h2>
              <p className="text-sm text-slate-600 dark:text-slate-400 mt-2 leading-relaxed">
                You've successfully answered all 20 mock interview questions. Let's send your session files to Gemini to compile your final feedback metrics.
              </p>
            </div>
            
            <button
              onClick={handleCompleteInterview}
              disabled={completing}
              className="flex items-center gap-2 rounded-lg bg-gradient-to-r from-indigo-500 to-purple-600 px-6 py-3.5 text-sm font-bold text-white shadow-lg shadow-indigo-500/25 hover:opacity-95 active:scale-[0.98] disabled:opacity-50 cursor-pointer"
            >
              {completing ? (
                <div className="h-5 w-5 animate-spin rounded-full border-2 border-white border-t-transparent" />
              ) : (
                <>
                  Compile Evaluation Report
                  <ChevronRight className="h-4.5 w-4.5" />
                </>
              )}
            </button>
          </div>
        ) : (
          <div className="flex-1 flex flex-col justify-between space-y-8">
            
            {/* Question Panel */}
            <div className="space-y-4">
              <div className="flex items-center gap-2 text-indigo-600 dark:text-indigo-400 font-semibold text-sm">
                <HelpCircle className="h-4.5 w-4.5" />
                <span>
                  {questionType === "mcq" ? "Multiple Choice Question:" : questionType === "fib" ? "Fill in the Blank Question:" : "Open-ended Question:"}
                </span>
              </div>
              <h2 className="text-xl font-bold text-slate-900 dark:text-slate-100 leading-relaxed pl-1">
                {questionText}
              </h2>
            </div>

            {/* Answer Panel */}
            <form onSubmit={handleSubmitAnswer} className="space-y-4">
              
              {questionType === "mcq" ? (
                // MCQ Option Blocks
                <div className="grid grid-cols-1 gap-3 pt-2">
                  {options.map((opt, index) => {
                    const letter = String.fromCharCode(65 + index); // A, B, C, D
                    const isSelected = answer === letter;
                    return (
                      <button
                        key={index}
                        type="button"
                        onClick={() => setAnswer(letter)}
                        disabled={submitting}
                        className={`flex items-start text-left p-4 rounded-xl border transition-all cursor-pointer ${
                          isSelected
                            ? "border-indigo-500 bg-indigo-500/10 text-slate-900 dark:text-white shadow-md shadow-indigo-500/5 font-semibold"
                            : "border-slate-200 bg-slate-50/70 text-slate-800 hover:border-slate-300 hover:bg-slate-100/70 dark:border-slate-800 dark:bg-slate-950/40 dark:text-slate-300 dark:hover:border-slate-700 dark:hover:bg-slate-900/20"
                        }`}
                      >
                        <span className={`flex h-6 w-6 shrink-0 items-center justify-center rounded-lg border text-xs font-bold mr-3 ${
                          isSelected
                            ? "bg-indigo-600 border-indigo-500 text-white"
                            : "bg-white border-slate-200 text-slate-700 dark:bg-slate-900 dark:border-slate-800 dark:text-slate-400"
                        }`}>
                          {letter}
                        </span>
                        <span className="text-sm font-medium leading-normal">{opt}</span>
                      </button>
                    );
                  })}
                </div>
              ) : (
                // Textarea for descriptive/FIB
                <div className="space-y-2">
                  <div className="flex justify-between items-center text-xs text-slate-500 pl-1">
                    <span>
                      {questionType === "fib"
                        ? "Provide the correct term to fill in the blank:"
                        : "Type your detailed answer below:"}
                    </span>
                    {questionType !== "fib" && (
                      <span className={wordCount < 10 ? "text-amber-600 dark:text-yellow-500/70 font-medium" : "text-indigo-600 dark:text-indigo-400/70 font-medium"}>
                        {wordCount} words (recommend 15+ words)
                      </span>
                    )}
                  </div>
                  
                  <textarea
                    ref={textareaRef}
                    required
                    rows={questionType === "fib" ? 3 : 6}
                    value={answer}
                    onChange={(e) => setAnswer(e.target.value)}
                    placeholder={
                      questionType === "fib"
                        ? "Type the missing word here..."
                        : "In my experience, I usually approach this by..."
                    }
                    disabled={submitting}
                    className="block w-full rounded-xl border border-slate-200 bg-slate-50 p-4 text-sm text-slate-900 placeholder-slate-400 outline-none transition-all focus:border-indigo-500 focus:ring-1 focus:ring-indigo-500 focus:bg-white dark:border-slate-800 dark:bg-slate-950/40 dark:text-slate-100 dark:placeholder-slate-600 dark:focus:bg-slate-950 disabled:opacity-50"
                    onKeyDown={(e) => {
                      if (e.key === "Enter" && e.ctrlKey) {
                        e.preventDefault();
                        handleSubmitAnswer(e);
                      }
                    }}
                  />
                </div>
              )}

              <div className="flex justify-between items-center">
                {questionType !== "mcq" && (
                  <span className="text-[10px] text-slate-500 italic hidden sm:inline">
                    Tip: Press Ctrl + Enter to submit answer
                  </span>
                )}
                
                <button
                  type="submit"
                  disabled={!answer.trim() || submitting}
                  className="flex items-center gap-2 rounded-lg bg-indigo-600 px-6 py-3 text-sm font-semibold text-white shadow-lg shadow-indigo-500/10 hover:bg-indigo-500 active:scale-[0.98] disabled:opacity-40 disabled:cursor-not-allowed cursor-pointer ml-auto"
                >
                  {submitting ? (
                    <div className="flex items-center gap-2">
                      <div className="h-4 w-4 animate-spin rounded-full border-2 border-white border-t-transparent" />
                      <span>Evaluating response...</span>
                    </div>
                  ) : (
                    <>
                      <span>Submit Answer</span>
                      <Send className="h-4 w-4" />
                    </>
                  )}
                </button>
              </div>
            </form>

          </div>
        )}
      </div>
    </div>
  );
};
export default Interview;
