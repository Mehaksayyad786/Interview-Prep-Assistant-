import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import { History, Calendar, ChevronRight, Search, SlidersHorizontal, AlertTriangle } from "lucide-react";

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

export const HistoryPage: React.FC = () => {
  const [history, setHistory] = useState<HistoryItem[]>([]);
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);

  // Filter states
  const [searchTerm, setSearchTerm] = useState<string>("");
  const [typeFilter, setTypeFilter] = useState<string>("All");
  const [diffFilter, setDiffFilter] = useState<string>("All");

  useEffect(() => {
    const fetchHistory = async () => {
      setLoading(true);
      setError(null);
      const token = localStorage.getItem("token");

      try {
        const response = await fetch("http://127.0.0.1:8000/api/history", {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        });

        if (response.ok) {
          const data = await response.json();
          setHistory(data);
        } else {
          setError("Failed to fetch interview log files.");
        }
      } catch (err) {
        setError("Network error. Make sure the API server is active.");
      } finally {
        setLoading(false);
      }
    };

    fetchHistory();
  }, []);

  const formatDate = (dateStr: string) => {
    const d = new Date(dateStr);
    return d.toLocaleDateString("en-US", {
      month: "short",
      day: "numeric",
      year: "numeric",
      hour: "2-digit",
      minute: "2-digit",
    });
  };

  // Filter logic
  const filteredHistory = history.filter((item) => {
    const matchesSearch = item.job_role.toLowerCase().includes(searchTerm.toLowerCase());
    const matchesType = typeFilter === "All" || item.interview_type === typeFilter;
    const matchesDiff = diffFilter === "All" || item.difficulty === diffFilter;
    return matchesSearch && matchesType && matchesDiff;
  });

  return (
    <div className="mx-auto max-w-7xl px-4 py-8 sm:px-6 lg:px-8 space-y-8">
      {/* Header */}
      <div>
        <h1 className="text-3xl font-extrabold tracking-tight text-slate-900 dark:text-white flex items-center gap-2">
          <History className="h-7 w-7 text-indigo-500" />
          Interview History
        </h1>
        <p className="mt-2 text-sm text-slate-600 dark:text-slate-400">
          Track your progress. View scores, evaluations, and weak topics of your previous sessions.
        </p>
      </div>

      {/* Filters bar */}
      <div className="rounded-2xl border border-slate-200 bg-white p-4 md:p-6 shadow-sm dark:border-slate-800 dark:bg-slate-900/60 dark:shadow-md backdrop-blur-xl flex flex-col md:flex-row md:items-center justify-between gap-4">
        
        {/* Search */}
        <div className="relative flex-1 max-w-md">
          <div className="pointer-events-none absolute inset-y-0 left-0 flex items-center pl-3">
            <Search className="h-4 w-4 text-slate-400 dark:text-slate-500" />
          </div>
          <input
            type="text"
            placeholder="Search by role..."
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
            className="block w-full rounded-lg border border-slate-200 bg-slate-50 py-2 pl-10 pr-3 text-sm text-slate-900 placeholder-slate-400 outline-none transition-all focus:border-indigo-500 focus:ring-1 focus:ring-indigo-500 focus:bg-white dark:border-slate-800 dark:bg-slate-950/50 dark:text-white dark:placeholder-slate-500 dark:focus:bg-slate-950"
          />
        </div>

        {/* Filters select */}
        <div className="flex flex-wrap items-center gap-4">
          <div className="flex items-center gap-2">
            <SlidersHorizontal className="h-4 w-4 text-slate-500 dark:text-slate-400 shrink-0" />
            <select
              value={typeFilter}
              onChange={(e) => setTypeFilter(e.target.value)}
              className="rounded-lg border border-slate-200 bg-white py-2 px-3 text-xs text-slate-900 outline-none transition-all focus:border-indigo-500 cursor-pointer dark:border-slate-800 dark:bg-slate-950 dark:text-white"
            >
              <option value="All" className="bg-white text-slate-900 dark:bg-slate-950 dark:text-white">All Categories</option>
              <option value="Technical" className="bg-white text-slate-900 dark:bg-slate-950 dark:text-white">Technical</option>
              <option value="HR" className="bg-white text-slate-900 dark:bg-slate-950 dark:text-white">HR</option>
              <option value="Behavioral" className="bg-white text-slate-900 dark:bg-slate-950 dark:text-white">Behavioral</option>
            </select>
          </div>

          <select
            value={diffFilter}
            onChange={(e) => setDiffFilter(e.target.value)}
            className="rounded-lg border border-slate-200 bg-white py-2 px-3 text-xs text-slate-900 outline-none transition-all focus:border-indigo-500 cursor-pointer dark:border-slate-800 dark:bg-slate-950 dark:text-white"
          >
            <option value="All" className="bg-white text-slate-900 dark:bg-slate-950 dark:text-white">All Difficulties</option>
            <option value="Easy" className="bg-white text-slate-900 dark:bg-slate-950 dark:text-white">Easy</option>
            <option value="Medium" className="bg-white text-slate-900 dark:bg-slate-950 dark:text-white">Medium</option>
            <option value="Hard" className="bg-white text-slate-900 dark:bg-slate-950 dark:text-white">Hard</option>
          </select>
        </div>
      </div>

      {error && (
        <div className="rounded-lg border border-red-500/30 bg-red-500/10 p-4 text-sm text-red-500 dark:text-red-400">
          {error}
        </div>
      )}

      {/* Main List */}
      <div className="rounded-2xl border border-slate-200 bg-white shadow-sm dark:border-slate-800 dark:bg-slate-900/60 dark:shadow-xl backdrop-blur-xl divide-y divide-slate-200 dark:divide-slate-800 overflow-hidden">
        {loading ? (
          <div className="flex justify-center items-center py-16">
            <div className="h-8 w-8 animate-spin rounded-full border-2 border-indigo-500 border-t-transparent" />
          </div>
        ) : filteredHistory.length === 0 ? (
          <div className="text-center py-16 px-4">
            <p className="text-slate-500 text-sm italic">No matching mock interview records found.</p>
            <Link
              to="/setup"
              className="inline-block mt-3 text-xs font-semibold text-indigo-600 dark:text-indigo-400 hover:text-indigo-500 dark:hover:text-indigo-300"
            >
              Launch a new mock session now &rarr;
            </Link>
          </div>
        ) : (
          filteredHistory.map((item) => (
            <div
              key={item.id}
              className="p-6 flex flex-col md:flex-row md:items-center justify-between gap-6 hover:bg-slate-50 dark:hover:bg-slate-900/30 transition-all"
            >
              {/* Left Column: Role Details */}
              <div className="space-y-2">
                <div className="flex items-center gap-2.5 flex-wrap">
                  <h3 className="text-base font-bold text-slate-900 dark:text-slate-200">{item.job_role}</h3>
                  <span className="rounded-full bg-indigo-50 border border-indigo-200 px-2.5 py-0.5 text-[10px] font-bold text-indigo-600 dark:bg-indigo-500/10 dark:border-indigo-500/20 dark:text-indigo-400">
                    {item.interview_type}
                  </span>
                  <span className="rounded-full bg-slate-100 border border-slate-200 px-2 py-0.5 text-[10px] font-medium text-slate-600 dark:bg-slate-950 dark:border-slate-800 dark:text-slate-500">
                    {item.difficulty}
                  </span>
                </div>
                <div className="flex items-center gap-1.5 text-xs text-slate-500">
                  <Calendar className="h-3.5 w-3.5" />
                  <span>{formatDate(item.date)}</span>
                </div>

                {/* Weak topics preview */}
                {item.status === "completed" && item.weak_topics.length > 0 && (
                  <div className="flex items-center gap-1.5 pt-1.5 flex-wrap">
                    <span className="text-[9px] text-slate-500 uppercase leading-none font-bold">Weak Areas:</span>
                    {item.weak_topics.map((t) => (
                      <span key={t} className="rounded bg-amber-500/10 border border-amber-500/20 px-1.5 py-0.5 text-[9px] text-amber-700 dark:text-yellow-500/80 dark:bg-yellow-500/5 dark:border-yellow-500/10 font-medium">
                        {t}
                      </span>
                    ))}
                  </div>
                )}
              </div>

              {/* Right Column: Score Actions */}
              <div className="flex items-center justify-between md:justify-end gap-6 border-t border-slate-100 dark:border-slate-900 pt-4 md:border-t-0 md:pt-0">
                {item.status === "completed" ? (
                  <div className="flex items-center gap-4">
                    <div className="text-right">
                      <span className="text-[10px] text-slate-500 block leading-none font-semibold uppercase">Score</span>
                      <span className="text-base font-extrabold text-indigo-600 dark:text-indigo-400">{item.overall_score}%</span>
                    </div>
                    <Link
                      to={`/results/${item.id}`}
                      className="flex items-center gap-1.5 rounded-lg border border-slate-200 bg-slate-50 px-4 py-2 text-xs font-semibold text-slate-700 hover:bg-slate-100 hover:text-slate-900 dark:border-slate-800 dark:bg-slate-950 dark:text-slate-300 dark:hover:bg-slate-800 dark:hover:text-white transition-all shadow-sm"
                    >
                      View Report
                      <ChevronRight className="h-3.5 w-3.5" />
                    </Link>
                  </div>
                ) : (
                  <div className="flex items-center gap-4">
                    <div className="flex items-center gap-1.5 text-xs text-amber-700 bg-amber-500/10 rounded border border-amber-500/20 px-2 py-0.5 dark:text-yellow-500 dark:bg-yellow-500/5 dark:border-yellow-500/15">
                      <AlertTriangle className="h-3.5 w-3.5 animate-pulse" />
                      <span>Incomplete</span>
                    </div>
                    <Link
                      to="/interview"
                      onClick={() => localStorage.setItem("current_interview_id", item.id)}
                      className="flex items-center gap-1.5 rounded-lg bg-indigo-600 px-4 py-2 text-xs font-semibold text-white hover:bg-indigo-500 transition-all shadow-md shadow-indigo-600/10"
                    >
                      Resume Mock
                      <ChevronRight className="h-3.5 w-3.5" />
                    </Link>
                  </div>
                )}
              </div>
            </div>
          ))
        )}
      </div>
    </div>
  );
};
export default HistoryPage;
