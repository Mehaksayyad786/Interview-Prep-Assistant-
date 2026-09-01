import React, { useState, useEffect } from "react";
import { useParams, useNavigate } from "react-router-dom";
import { Trophy, ChevronLeft, AlertTriangle, ChevronDown, ChevronUp, Sparkles, BookOpen } from "lucide-react";

interface QuestionAnswerDetail {
  question_number: number;
  question: string;
  answer: string | null;
  technical_score: number | null;
  communication_score: number | null;
  relevance_score: number | null;
  feedback: string | null;
  weak_topic: string | null;
}

interface ResultsData {
  interview_id: string;
  overall_score: number;
  technical_score: number;
  communication_score: number;
  relevance_score: number;
  weak_topics: string[];
  improvement_plan: string[];
  questions: QuestionAnswerDetail[];
  interview_type?: string;
}

const CircularProgress: React.FC<{ score: number; label: string; color: string; strokeColor: string }> = ({ score, label, color, strokeColor }) => {
  const radius = 32;
  const circumference = 2 * Math.PI * radius;
  const offset = circumference - (score / 100) * circumference;

  return (
    <div className="flex flex-col items-center gap-3 p-4 rounded-xl border border-slate-200 bg-slate-50/70 dark:border-slate-900 dark:bg-slate-950/40 w-full shadow-sm">
      <div className="relative flex items-center justify-center">
        <svg className="h-20 w-20 transform -rotate-90">
          <circle
            cx="40"
            cy="40"
            r={radius}
            className="stroke-slate-200 dark:stroke-slate-900 fill-none"
            strokeWidth="6"
          />
          <circle
            cx="40"
            cy="40"
            r={radius}
            className={`fill-none transition-all duration-1000 ${strokeColor}`}
            strokeWidth="6"
            strokeDasharray={circumference}
            strokeDashoffset={offset}
            strokeLinecap="round"
          />
        </svg>
        <span className={`absolute text-base font-extrabold ${color}`}>{score}%</span>
      </div>
      <span className="text-[10px] font-bold text-slate-600 dark:text-slate-400 uppercase tracking-wider">{label}</span>
    </div>
  );
};

export const Results: React.FC = () => {
  const { interviewId } = useParams<{ interviewId: string }>();
  const navigate = useNavigate();
  const [data, setData] = useState<ResultsData | null>(null);
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);
  const [expandedQuestion, setExpandedQuestion] = useState<number | null>(null);

  const getTechnicalLabel = () => {
    if (!data) return "Technical";
    if (data.interview_type === "HR") return "HR Skills";
    if (data.interview_type === "Behavioral") return "Behavioral";
    return "Technical";
  };

  useEffect(() => {
    const fetchResults = async () => {
      if (!interviewId) return;
      const token = localStorage.getItem("token");

      try {
        const response = await fetch(`http://127.0.0.1:8000/api/results/${interviewId}`, {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        });

        const resData = await response.json();

        if (response.ok) {
          setData(resData);
        } else {
          setError(resData.detail || "Failed to load results.");
        }
      } catch (err) {
        setError("Network error. Could not retrieve result files.");
      } finally {
        setLoading(false);
      }
    };

    fetchResults();
  }, [interviewId]);

  const toggleQuestion = (num: number) => {
    setExpandedQuestion(expandedQuestion === num ? null : num);
  };

  if (loading) {
    return (
      <div className="flex min-h-[calc(100vh-4rem)] items-center justify-center bg-slate-50 dark:bg-slate-950">
        <div className="flex flex-col items-center gap-3">
          <div className="h-8 w-8 animate-spin rounded-full border-2 border-indigo-500 border-t-transparent" />
          <p className="text-sm text-slate-600 dark:text-slate-400 animate-pulse font-medium">Fetching your report summary...</p>
        </div>
      </div>
    );
  }

  if (error || !data) {
    return (
      <div className="mx-auto max-w-4xl px-4 py-8 text-center space-y-4">
        <div className="inline-block p-3 rounded-full bg-red-500/10 text-red-500">
          <AlertTriangle className="h-8 w-8" />
        </div>
        <h2 className="text-xl font-bold text-slate-900 dark:text-white">Failed to load reports</h2>
        <p className="text-sm text-slate-600 dark:text-slate-400">{error || "Interview details not found."}</p>
        <button
          onClick={() => navigate("/")}
          className="inline-block text-xs font-semibold text-indigo-600 dark:text-indigo-400 hover:underline cursor-pointer"
        >
          Return to Dashboard
        </button>
      </div>
    );
  }

  return (
    <div className="mx-auto max-w-5xl px-4 py-8 sm:px-6 lg:px-8 space-y-8">
      {/* Header */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
        <div>
          <button
            onClick={() => navigate("/")}
            className="mb-4 flex items-center gap-1.5 text-xs text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-slate-200 transition-colors cursor-pointer"
          >
            <ChevronLeft className="h-4 w-4" />
            Back to Dashboard
          </button>
          <h1 className="text-3xl font-extrabold tracking-tight text-slate-900 dark:text-white flex items-center gap-2">
            <Trophy className="h-7 w-7 text-indigo-500 animate-bounce" />
            Performance Evaluation
          </h1>
          <p className="mt-1 text-sm text-slate-600 dark:text-slate-400">
            Session report for your mock interview. Review scores and improvement plans.
          </p>
        </div>
      </div>

      {/* Overview Card: Final Score */}
      <div className="rounded-2xl border border-slate-200 bg-white p-6 md:p-8 shadow-sm dark:border-slate-800 dark:bg-slate-900/60 dark:shadow-xl backdrop-blur-xl grid grid-cols-1 lg:grid-cols-3 gap-8 items-center">
        {/* Main overall gauge */}
        <div className="flex flex-col items-center justify-center text-center lg:border-r lg:border-slate-200 dark:lg:border-slate-800 lg:pr-8 py-4 space-y-4">
          <span className="text-xs font-bold text-slate-500 dark:text-slate-400 uppercase tracking-wider">Overall Performance</span>
          <div className="relative flex items-center justify-center">
            <svg className="h-32 w-32 transform -rotate-90">
              <circle
                cx="64"
                cy="64"
                r="52"
                className="stroke-slate-100 dark:stroke-slate-950 fill-none"
                strokeWidth="10"
              />
              <circle
                cx="64"
                cy="64"
                r="52"
                className="fill-none stroke-indigo-500 transition-all duration-1000"
                strokeWidth="10"
                strokeDasharray={2 * Math.PI * 52}
                strokeDashoffset={2 * Math.PI * 52 - (data.overall_score / 100) * 2 * Math.PI * 52}
                strokeLinecap="round"
              />
            </svg>
            <span className="absolute text-3xl font-extrabold text-slate-900 dark:text-white">{data.overall_score}%</span>
          </div>
          <span className="text-xs text-slate-500">Average of all evaluated metrics</span>
        </div>

        {/* Category gauges */}
        <div className="lg:col-span-2 space-y-4">
          <h4 className="text-xs font-semibold text-slate-500 dark:text-slate-400 uppercase tracking-wider pl-1">Metrics Breakdown</h4>
          <div className="grid grid-cols-1 sm:grid-cols-3 gap-4">
            <CircularProgress score={data.technical_score} label={getTechnicalLabel()} color="text-indigo-600 dark:text-indigo-400" strokeColor="stroke-indigo-500" />
            <CircularProgress score={data.communication_score} label="Communication" color="text-purple-600 dark:text-purple-400" strokeColor="stroke-purple-500" />
            <CircularProgress score={data.relevance_score} label="Relevance" color="text-pink-600 dark:text-pink-400" strokeColor="stroke-pink-500" />
          </div>
        </div>
      </div>

      {/* Weak topics & Personalized Roadmap */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        {/* Weak topics */}
        <div className="rounded-2xl border border-slate-200 bg-white p-6 shadow-sm dark:border-slate-800 dark:bg-slate-900/60 dark:shadow-xl backdrop-blur-xl space-y-4">
          <h3 className="text-base font-bold text-slate-900 dark:text-white flex items-center gap-2">
            <AlertTriangle className="h-5 w-5 text-amber-500 dark:text-yellow-500" />
            Weak Areas Identified
          </h3>
          <p className="text-xs text-slate-600 dark:text-slate-400 leading-relaxed">
            The AI analyzed your submitted answers. You received the lowest points in these specific topic domains:
          </p>

          <div className="flex flex-wrap gap-2 pt-2">
            {data.weak_topics.length === 0 ? (
              <span className="text-xs text-slate-500 italic">No critical weak areas identified! Outstanding work.</span>
            ) : (
              data.weak_topics.map((topic) => (
                <span
                  key={topic}
                  className="rounded-lg border border-amber-500/30 bg-amber-500/10 px-3.5 py-2 text-xs font-bold text-amber-700 dark:text-yellow-400 dark:border-yellow-500/20 dark:bg-yellow-500/5"
                >
                  {topic}
                </span>
              ))
            )}
          </div>
        </div>

        {/* Action roadmap */}
        <div className="rounded-2xl border border-slate-200 bg-white p-6 shadow-sm dark:border-slate-800 dark:bg-slate-900/60 dark:shadow-xl backdrop-blur-xl space-y-4">
          <h3 className="text-base font-bold text-slate-900 dark:text-white flex items-center gap-2">
            <Sparkles className="h-5 w-5 text-indigo-600 dark:text-indigo-400" />
            Personalized Improvement Plan
          </h3>
          <p className="text-xs text-slate-600 dark:text-slate-400 leading-relaxed">
            Follow this customized checklist recommended by Gemini to improve your interview outcomes:
          </p>

          <div className="space-y-3 pt-2">
            {data.improvement_plan.map((item, idx) => (
              <div key={idx} className="flex gap-3">
                <span className="flex h-5 w-5 shrink-0 items-center justify-center rounded-md bg-indigo-500/10 text-[10px] font-bold text-indigo-600 dark:text-indigo-400">
                  {idx + 1}
                </span>
                <span className="text-xs text-slate-700 dark:text-slate-300 leading-relaxed">{item}</span>
              </div>
            ))}
          </div>
        </div>
      </div>

      {/* Questions Breakdown list */}
      <div className="rounded-2xl border border-slate-200 bg-white p-6 shadow-sm dark:border-slate-800 dark:bg-slate-900/60 dark:shadow-xl backdrop-blur-xl space-y-4">
        <h3 className="text-base font-bold text-slate-900 dark:text-white flex items-center gap-2">
          <BookOpen className="h-5 w-5 text-indigo-500" />
          Question-by-Question Breakdown
        </h3>
        
        <div className="space-y-3 pt-2">
          {data.questions.map((qa) => {
            const isExpanded = expandedQuestion === qa.question_number;
            const avgQScore = Math.round(
              ((qa.technical_score || 0) + (qa.communication_score || 0) + (qa.relevance_score || 0)) / 3
            );

            return (
              <div
                key={qa.question_number}
                className="rounded-xl border border-slate-200 bg-slate-50/50 dark:border-slate-800 dark:bg-slate-950/20 overflow-hidden"
              >
                {/* Header/Toggler */}
                <button
                  onClick={() => toggleQuestion(qa.question_number)}
                  className="w-full flex items-center justify-between p-4 text-left hover:bg-slate-100/60 dark:hover:bg-slate-900/20 transition-all cursor-pointer"
                >
                  <div className="space-y-1 pr-4">
                    <span className="text-[10px] font-bold text-indigo-600 dark:text-indigo-400 uppercase tracking-wider block">
                      Question {qa.question_number}
                    </span>
                    <span className="text-sm font-semibold text-slate-800 dark:text-slate-200 line-clamp-1">
                      {qa.question}
                    </span>
                  </div>

                  <div className="flex items-center gap-4 shrink-0">
                    <span className="text-xs font-bold text-indigo-700 bg-indigo-50 border border-indigo-200 rounded px-2 py-0.5 dark:text-indigo-300 dark:bg-indigo-500/5 dark:border-indigo-500/10">
                      Score: {avgQScore}%
                    </span>
                    {isExpanded ? <ChevronUp className="h-4 w-4 text-slate-500" /> : <ChevronDown className="h-4 w-4 text-slate-500" />}
                  </div>
                </button>

                {/* Expanded details */}
                {isExpanded && (
                  <div className="border-t border-slate-200 bg-white p-4 space-y-4 dark:border-slate-800 dark:bg-slate-950/40">
                    {/* Candidate answer */}
                    <div className="space-y-1.5">
                      <span className="text-[10px] text-slate-500 uppercase leading-none font-semibold block">Your Answer:</span>
                      <p className="text-xs text-slate-800 bg-slate-50 p-3 rounded-lg border border-slate-200 leading-relaxed dark:text-slate-300 dark:bg-slate-950 dark:border-slate-900">
                        {qa.answer || "No answer submitted."}
                      </p>
                    </div>

                    {/* Scores row */}
                    <div className="grid grid-cols-3 gap-2">
                      <div className="p-2 border border-slate-200 bg-slate-50/70 rounded-lg text-center dark:border-slate-900 dark:bg-slate-950/30">
                        <span className="text-[9px] text-slate-500 block">{getTechnicalLabel()}</span>
                        <span className="text-xs font-bold text-indigo-600 dark:text-indigo-400">{qa.technical_score}%</span>
                      </div>
                      <div className="p-2 border border-slate-200 bg-slate-50/70 rounded-lg text-center dark:border-slate-900 dark:bg-slate-950/30">
                        <span className="text-[9px] text-slate-500 block">Communication</span>
                        <span className="text-xs font-bold text-purple-600 dark:text-purple-400">{qa.communication_score}%</span>
                      </div>
                      <div className="p-2 border border-slate-200 bg-slate-50/70 rounded-lg text-center dark:border-slate-900 dark:bg-slate-950/30">
                        <span className="text-[9px] text-slate-500 block">Relevance</span>
                        <span className="text-xs font-bold text-pink-600 dark:text-pink-400">{qa.relevance_score}%</span>
                      </div>
                    </div>

                    {/* AI Feedback */}
                    <div className="space-y-1.5">
                      <span className="text-[10px] text-slate-500 uppercase leading-none font-semibold block">AI Evaluator Feedback:</span>
                      <p className="text-xs text-slate-700 dark:text-slate-300 leading-relaxed">
                        {qa.feedback || "Feedback not calculated."}
                      </p>
                    </div>

                    {/* Weak topic category */}
                    {qa.weak_topic && (
                      <div className="flex items-center gap-1.5 text-xs text-amber-700 bg-amber-500/10 rounded-lg border border-amber-500/20 px-3 py-1.5 self-start w-fit dark:text-yellow-400 dark:bg-yellow-500/5 dark:border-yellow-500/10">
                        <AlertTriangle className="h-3.5 w-3.5" />
                        <span>Syllabus weakness: <strong>{qa.weak_topic}</strong></span>
                      </div>
                    )}

                  </div>
                )}
              </div>
            );
          })}
        </div>
      </div>
    </div>
  );
};
export default Results;
