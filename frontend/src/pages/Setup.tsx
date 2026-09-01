import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { useAuth } from "../context/AuthContext";
import { Sparkles, ArrowRight, ChevronLeft, Target } from "lucide-react";

const TARGET_ROLES = [
  "Python Developer",
  "Java Developer",
  "Data Analyst",
  "Data Scientist",
  "Machine Learning Engineer",
  "AI Engineer",
];

const INTERVIEW_TYPES = [
  { id: "Technical", label: "Technical Interview", desc: "Covers programming, database queries, and tech architectures." },
  { id: "HR", label: "HR Interview", desc: "Focuses on personal goals, background, and cultural fit." },
  { id: "Behavioral", label: "Behavioral Interview", desc: "Situational questions using the STAR framework." },
];

const DIFFICULTY_LEVELS = ["Easy", "Medium", "Hard"];

export const Setup: React.FC = () => {
  const { user } = useAuth();
  const navigate = useNavigate();

  // Selected configs
  const [jobRole, setJobRole] = useState<string>("");
  const [interviewType, setInterviewType] = useState<string>("Technical");
  const [difficulty, setDifficulty] = useState<string>("Medium");
  
  // UI states
  const [loading, setLoading] = useState<boolean>(false);
  const [error, setError] = useState<string | null>(null);

  // Sync default job role with preferred role
  useEffect(() => {
    if (user?.preferred_job_role) {
      setJobRole(user.preferred_job_role);
    } else {
      setJobRole(TARGET_ROLES[0]);
    }
  }, [user]);

  const handleStart = async (e: React.FormEvent) => {
    e.preventDefault();
    setError(null);
    setLoading(true);

    const token = localStorage.getItem("token");
    if (!token) {
      setError("Please log in to continue.");
      setLoading(false);
      return;
    }

    try {
      const response = await fetch("http://127.0.0.1:8000/api/interview/start", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${token}`,
        },
        body: JSON.stringify({
          job_role: jobRole,
          interview_type: interviewType,
          difficulty: difficulty,
        }),
      });

      const data = await response.json();

      if (response.ok) {
        // Save current active interview id to localStorage
        localStorage.setItem("current_interview_id", data.id);
        navigate("/interview");
      } else {
        setError(data.detail || "Failed to start interview. Please try again.");
      }
    } catch (err) {
      setError("Network connection issue. Make sure the backend is active.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="mx-auto max-w-4xl px-4 py-8 sm:px-6 lg:px-8">
      {/* Back button */}
      <button
        onClick={() => navigate("/")}
        className="mb-6 flex items-center gap-1.5 text-xs text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-slate-200 transition-colors cursor-pointer"
      >
        <ChevronLeft className="h-4 w-4" />
        Back to Dashboard
      </button>

      {/* Header */}
      <div className="mb-8">
        <h1 className="text-3xl font-extrabold tracking-tight text-slate-900 dark:text-white flex items-center gap-2">
          <Target className="h-7 w-7 text-indigo-500" />
          Configure Mock Interview
        </h1>
        <p className="mt-2 text-sm text-slate-600 dark:text-slate-400">
          Tailor your mock session below. AI will customize the generated questions accordingly.
        </p>
      </div>

      {error && (
        <div className="mb-6 rounded-lg border border-red-500/30 bg-red-500/10 p-4 text-sm text-red-500 dark:text-red-400">
          {error}
        </div>
      )}

      {/* Configuration Wizard Form */}
      <form onSubmit={handleStart} className="space-y-6">
        
        {/* Step 1: Select Role */}
        <div className="rounded-2xl border border-slate-200 bg-white p-6 md:p-8 shadow-sm dark:border-slate-800 dark:bg-slate-900/60 dark:shadow-xl space-y-4">
          <div className="flex items-center gap-2 border-b border-slate-200 dark:border-slate-800 pb-3">
            <span className="flex h-6 w-6 items-center justify-center rounded-full bg-indigo-500/10 text-indigo-600 dark:text-indigo-400 text-xs font-bold">1</span>
            <h3 className="text-sm font-semibold text-slate-900 dark:text-white">Target Job Role</h3>
          </div>
          
          <div className="space-y-2">
            <label className="text-xs text-slate-600 dark:text-slate-400" htmlFor="role">
              Which role are you practicing for?
            </label>
            <select
              id="role"
              value={jobRole}
              onChange={(e) => setJobRole(e.target.value)}
              className="block w-full rounded-lg border border-slate-200 bg-slate-50 py-3 px-4 text-sm text-slate-900 outline-none transition-all focus:border-indigo-500 focus:ring-1 focus:ring-indigo-500 focus:bg-white dark:border-slate-800 dark:bg-slate-950 dark:text-white cursor-pointer"
            >
              {TARGET_ROLES.map((role) => (
                <option key={role} value={role} className="bg-white text-slate-900 dark:bg-slate-950 dark:text-white">
                  {role}
                </option>
              ))}
            </select>
          </div>
        </div>

        {/* Step 2: Select Interview Type */}
        <div className="rounded-2xl border border-slate-200 bg-white p-6 md:p-8 shadow-sm dark:border-slate-800 dark:bg-slate-900/60 dark:shadow-xl space-y-4">
          <div className="flex items-center gap-2 border-b border-slate-200 dark:border-slate-800 pb-3">
            <span className="flex h-6 w-6 items-center justify-center rounded-full bg-indigo-500/10 text-indigo-600 dark:text-indigo-400 text-xs font-bold">2</span>
            <h3 className="text-sm font-semibold text-slate-900 dark:text-white">Interview Category</h3>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
            {INTERVIEW_TYPES.map((type) => (
              <button
                key={type.id}
                type="button"
                onClick={() => setInterviewType(type.id)}
                className={`flex flex-col text-left p-4 rounded-xl border transition-all cursor-pointer ${
                  interviewType === type.id
                    ? "border-indigo-500 bg-indigo-500/10 shadow-md shadow-indigo-500/10 dark:bg-indigo-500/5"
                    : "border-slate-200 bg-slate-50/70 hover:border-slate-300 hover:bg-slate-100/70 dark:border-slate-800 dark:bg-slate-950/30 dark:hover:border-slate-700 dark:hover:bg-slate-900/30"
                }`}
              >
                <span className={`text-xs font-bold ${interviewType === type.id ? "text-indigo-600 dark:text-indigo-400" : "text-slate-800 dark:text-slate-200"}`}>
                  {type.label}
                </span>
                <span className="text-[11px] text-slate-500 dark:text-slate-400 mt-2 leading-relaxed">
                  {type.desc}
                </span>
              </button>
            ))}
          </div>
        </div>

        {/* Step 3: Difficulty */}
        <div className="rounded-2xl border border-slate-200 bg-white p-6 md:p-8 shadow-sm dark:border-slate-800 dark:bg-slate-900/60 dark:shadow-xl space-y-4">
          <div className="flex items-center gap-2 border-b border-slate-200 dark:border-slate-800 pb-3">
            <span className="flex h-6 w-6 items-center justify-center rounded-full bg-indigo-500/10 text-indigo-600 dark:text-indigo-400 text-xs font-bold">3</span>
            <h3 className="text-sm font-semibold text-slate-900 dark:text-white">Difficulty Level</h3>
          </div>

          <div className="flex rounded-lg bg-slate-100 p-1 border border-slate-200 dark:bg-slate-950 dark:border-slate-900 w-full sm:w-80">
            {DIFFICULTY_LEVELS.map((lvl) => (
              <button
                key={lvl}
                type="button"
                onClick={() => setDifficulty(lvl)}
                className={`w-1/3 rounded-md py-2.5 text-xs font-semibold transition-all cursor-pointer ${
                  difficulty === lvl
                    ? "bg-indigo-600 text-white shadow-md shadow-indigo-600/20"
                    : "text-slate-600 hover:text-slate-900 dark:text-slate-400 dark:hover:text-slate-200"
                }`}
              >
                {lvl}
              </button>
            ))}
          </div>
        </div>

        {/* Launch */}
        <div className="flex justify-end pt-2">
          <button
            type="submit"
            disabled={loading}
            className="flex items-center gap-2 rounded-lg bg-indigo-600 px-8 py-3.5 text-sm font-bold text-white shadow-lg shadow-indigo-500/20 hover:bg-indigo-500 active:scale-[0.98] transition-all disabled:opacity-50 cursor-pointer"
          >
            {loading ? (
              <div className="h-5 w-5 animate-spin rounded-full border-2 border-white border-t-transparent" />
            ) : (
              <>
                <Sparkles className="h-4.5 w-4.5" />
                Launch Mock Session
                <ArrowRight className="h-4.5 w-4.5" />
              </>
            )}
          </button>
        </div>
      </form>
    </div>
  );
};
export default Setup;
