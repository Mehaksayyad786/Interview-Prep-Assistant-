import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import { useAuth } from "../context/AuthContext";
import { Sparkles, Briefcase, GraduationCap, Code, ArrowRight, Activity, Calendar, Trophy, ChevronRight } from "lucide-react";

interface HistoryItem {
  id: string;
  job_role: string;
  interview_type: string;
  difficulty: string;
  status: string;
  date: string;
  overall_score: number | null;
  weak_topics: string[];
}

export const Dashboard: React.FC = () => {
  const { user } = useAuth();
  const [history, setHistory] = useState<HistoryItem[]>([]);
  const [loading, setLoading] = useState<boolean>(true);

  useEffect(() => {
    const fetchHistory = async () => {
      const token = localStorage.getItem("token");
      if (!token) return;

      try {
        const response = await fetch("http://127.0.0.1:8000/api/history", {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        });

        if (response.ok) {
          const data = await response.json();
          setHistory(data);
        }
      } catch (error) {
        console.error("Failed to load history on dashboard:", error);
      } finally {
        setLoading(false);
      }
    };

    fetchHistory();
  }, []);

  const completedInterviews = history.filter((h) => h.status === "completed");
  const totalCompleted = completedInterviews.length;
  
  const averageScore = totalCompleted > 0
    ? Math.round(completedInterviews.reduce((acc, curr) => acc + (curr.overall_score || 0), 0) / totalCompleted)
    : 0;

  const isProfileIncomplete = !user?.preferred_job_role || user.preferred_job_role === "";

  const formatDate = (dateStr: string) => {
    const d = new Date(dateStr);
    return d.toLocaleDateString("en-US", { month: "short", day: "numeric", year: "numeric" });
  };

  return (
    <div className="mx-auto max-w-7xl px-4 py-8 sm:px-6 lg:px-8 space-y-8">
      {/* Welcome Banner */}
      <div className="flex flex-col md:flex-row md:items-center justify-between gap-4">
        <div>
          <h1 className="text-3xl font-extrabold tracking-tight text-slate-900 dark:text-white">
            Hello, {user?.name || "Candidate"}!
          </h1>
          <p className="mt-1.5 text-sm text-slate-600 dark:text-slate-400">
            Welcome to your interview dashboard. Ready to practice and build your skills?
          </p>
        </div>
        <Link
          to="/setup"
          className="flex items-center gap-1.5 self-start md:self-auto rounded-lg bg-indigo-600 px-5 py-3 text-sm font-semibold text-white shadow-lg shadow-indigo-500/20 hover:bg-indigo-500 active:scale-[0.97] transition-all cursor-pointer"
        >
          <Sparkles className="h-4 w-4" />
          Start Mock Interview
          <ArrowRight className="h-4 w-4" />
        </Link>
      </div>

      {/* Profile Incomplete Warning Banner */}
      {isProfileIncomplete && (
        <div className="rounded-xl border border-yellow-500/30 bg-yellow-500/10 p-4 flex flex-col sm:flex-row sm:items-center justify-between gap-3">
          <div className="flex items-start gap-3">
            <div className="flex h-9 w-9 shrink-0 items-center justify-center rounded-lg bg-yellow-500/20 text-yellow-600 dark:text-yellow-400">
              <GraduationCap className="h-5 w-5" />
            </div>
            <div>
              <h4 className="text-sm font-semibold text-yellow-700 dark:text-yellow-400">Incomplete Profile</h4>
              <p className="text-xs text-slate-600 dark:text-slate-400 mt-0.5">
                Set up your profile with your target role and skills to receive highly relevant AI questions.
              </p>
            </div>
          </div>
          <Link
            to="/profile"
            className="text-xs font-semibold text-indigo-600 dark:text-indigo-400 hover:text-indigo-500 dark:hover:text-indigo-300 flex items-center gap-1 border border-indigo-500/20 rounded-lg px-3 py-1.5 bg-indigo-500/5 transition-all self-start sm:self-auto shrink-0"
          >
            Update Profile
            <ChevronRight className="h-3 w-3" />
          </Link>
        </div>
      )}

      {/* Grid: Stats & Profile Summary */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        
        {/* Statistics Cards */}
        <div className="lg:col-span-2 grid grid-cols-1 sm:grid-cols-2 gap-6">
          <div className="rounded-2xl border border-slate-200 bg-white p-6 flex items-center justify-between shadow-sm dark:border-slate-800 dark:bg-slate-900/60 dark:shadow-lg">
            <div className="space-y-2">
              <span className="text-xs font-medium text-slate-500 dark:text-slate-400">Total Interviews Taken</span>
              <h2 className="text-4xl font-extrabold text-slate-900 dark:text-white">{totalCompleted}</h2>
              <span className="text-[11px] text-slate-500">Completed feedback sessions</span>
            </div>
            <div className="flex h-12 w-12 items-center justify-center rounded-xl bg-purple-500/10 text-purple-600 dark:text-purple-400 shadow-sm">
              <Activity className="h-6 w-6" />
            </div>
          </div>

          <div className="rounded-2xl border border-slate-200 bg-white p-6 flex items-center justify-between shadow-sm dark:border-slate-800 dark:bg-slate-900/60 dark:shadow-lg">
            <div className="space-y-2">
              <span className="text-xs font-medium text-slate-500 dark:text-slate-400">Average Performance</span>
              <h2 className="text-4xl font-extrabold text-indigo-600 dark:text-indigo-400">
                {averageScore}%
              </h2>
              <span className="text-[11px] text-slate-500">Calculated over all mocks</span>
            </div>
            <div className="flex h-12 w-12 items-center justify-center rounded-xl bg-indigo-500/10 text-indigo-600 dark:text-indigo-400 shadow-sm">
              <Trophy className="h-6 w-6" />
            </div>
          </div>
        </div>

        {/* Profile Card */}
        <div className="rounded-2xl border border-slate-200 bg-white p-6 shadow-sm dark:border-slate-800 dark:bg-slate-900/60 dark:shadow-lg space-y-4">
          <div className="flex items-center justify-between">
            <h3 className="text-sm font-semibold text-slate-900 dark:text-white">Target Summary</h3>
            <Link to="/profile" className="text-xs text-indigo-600 dark:text-indigo-400 hover:text-indigo-500 dark:hover:text-indigo-300 transition-colors font-medium">
              Edit
            </Link>
          </div>
          
          <div className="space-y-3.5 pt-1.5">
            <div className="flex items-center gap-3">
              <Briefcase className="h-4.5 w-4.5 text-slate-400 dark:text-slate-500" />
              <div>
                <p className="text-[10px] text-slate-500 uppercase leading-none font-semibold">Target Job Role</p>
                <p className="text-xs font-medium text-slate-800 dark:text-slate-300 mt-1">
                  {user?.preferred_job_role || "Not specified"}
                </p>
              </div>
            </div>

            <div className="flex items-center gap-3">
              <GraduationCap className="h-4.5 w-4.5 text-slate-400 dark:text-slate-500" />
              <div>
                <p className="text-[10px] text-slate-500 uppercase leading-none font-semibold">Education & Exp</p>
                <p className="text-xs font-medium text-slate-800 dark:text-slate-300 mt-1">
                  {user?.education || "Not specified"} ({user?.experience_level || "Fresher"})
                </p>
              </div>
            </div>

            <div className="flex items-start gap-3">
              <Code className="h-4.5 w-4.5 text-slate-400 dark:text-slate-500 mt-0.5" />
              <div>
                <p className="text-[10px] text-slate-500 uppercase leading-none font-semibold">Configured Skills</p>
                <div className="flex flex-wrap gap-1 mt-1.5">
                  {user?.skills && user.skills.length > 0 ? (
                    user.skills.map((s) => (
                      <span key={s} className="rounded-full bg-slate-100 border border-slate-200 px-2 py-0.5 text-[10px] text-slate-700 dark:bg-slate-950 dark:border-slate-800 dark:text-slate-400">
                        {s}
                      </span>
                    ))
                  ) : (
                    <span className="text-xs text-slate-400 italic">None added</span>
                  )}
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      {/* Recent Mocks list */}
      <div className="rounded-2xl border border-slate-200 bg-white shadow-sm dark:border-slate-800 dark:bg-slate-900/60 dark:shadow-lg">
        <div className="px-6 py-5 border-b border-slate-200 dark:border-slate-800 flex items-center justify-between">
          <h3 className="text-base font-semibold text-slate-900 dark:text-white">Recent Mock Interviews</h3>
          <Link to="/history" className="text-xs text-indigo-600 dark:text-indigo-400 hover:text-indigo-500 dark:hover:text-indigo-300 transition-colors font-medium">
            View All History
          </Link>
        </div>

        <div className="divide-y divide-slate-200 dark:divide-slate-800 overflow-hidden">
          {loading ? (
            <div className="flex items-center justify-center py-12">
              <div className="h-6 w-6 animate-spin rounded-full border-2 border-indigo-500 border-t-transparent" />
            </div>
          ) : history.length === 0 ? (
            <div className="text-center py-12 px-4">
              <p className="text-slate-500 text-sm italic">You haven't taken any interviews yet.</p>
              <Link
                to="/setup"
                className="inline-block mt-3 text-xs font-semibold text-indigo-600 dark:text-indigo-400 hover:text-indigo-500 dark:hover:text-indigo-300"
              >
                Launch your first mock session now &rarr;
              </Link>
            </div>
          ) : (
            history.slice(0, 4).map((item) => (
              <div
                key={item.id}
                className="p-6 flex flex-col sm:flex-row sm:items-center justify-between gap-4 transition-all hover:bg-slate-50 dark:hover:bg-slate-900/40"
              >
                <div className="space-y-1.5">
                  <div className="flex items-center gap-2">
                    <span className="font-semibold text-slate-800 dark:text-slate-200 text-sm">
                      {item.job_role}
                    </span>
                    <span className="rounded-full bg-slate-100 border border-slate-200 px-2 py-0.5 text-[9px] font-medium text-slate-600 dark:bg-slate-950 dark:border-slate-800 dark:text-slate-400">
                      {item.interview_type}
                    </span>
                  </div>
                  <div className="flex items-center gap-4 text-xs text-slate-500">
                    <span className="flex items-center gap-1">
                      <Calendar className="h-3.5 w-3.5" />
                      {formatDate(item.date)}
                    </span>
                    <span>Diff: {item.difficulty}</span>
                  </div>
                </div>

                <div className="flex items-center justify-between sm:justify-end gap-6">
                  {item.status === "completed" ? (
                    <div className="flex items-center gap-2.5">
                      <div className="text-right">
                        <span className="text-[10px] text-slate-500 block leading-none font-semibold uppercase">Score</span>
                        <span className="text-sm font-bold text-indigo-600 dark:text-indigo-400">{item.overall_score}%</span>
                      </div>
                      <Link
                        to={`/results/${item.id}`}
                        className="flex items-center gap-1 rounded-lg border border-slate-200 bg-slate-50 px-3 py-1.5 text-xs text-slate-700 hover:bg-slate-100 hover:text-slate-900 dark:border-slate-800 dark:bg-slate-950 dark:text-slate-300 dark:hover:bg-slate-800 dark:hover:text-white transition-all shadow-sm"
                      >
                        Report
                        <ChevronRight className="h-3 w-3" />
                      </Link>
                    </div>
                  ) : (
                    <div className="flex items-center gap-3">
                      <span className="rounded-full bg-yellow-500/10 border border-yellow-500/20 px-2 py-0.5 text-[10px] font-medium text-yellow-600 dark:text-yellow-500">
                        In Progress
                      </span>
                      <Link
                        to="/interview"
                        onClick={() => localStorage.setItem("current_interview_id", item.id)}
                        className="flex items-center gap-1 rounded-lg bg-indigo-600/10 border border-indigo-500/20 px-3 py-1.5 text-xs text-indigo-600 dark:text-indigo-300 hover:bg-indigo-600 hover:text-white transition-all"
                      >
                        Resume
                        <ChevronRight className="h-3 w-3" />
                      </Link>
                    </div>
                  )}
                </div>
              </div>
            ))
          )}
        </div>
      </div>
    </div>
  );
};
export default Dashboard;
