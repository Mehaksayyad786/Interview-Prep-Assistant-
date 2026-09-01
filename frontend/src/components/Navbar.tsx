import React from "react";
import { Link, useLocation } from "react-router-dom";
import { useAuth } from "../context/AuthContext";
import { User, LogOut, LayoutDashboard, History, Sparkles } from "lucide-react";
import { ThemeToggle } from "./ThemeToggle";

export const Navbar: React.FC = () => {
  const { user, logout } = useAuth();
  const location = useLocation();

  if (!user) return null;

  const isActive = (path: string) => location.pathname === path;

  return (
    <nav className="sticky top-0 z-50 w-full border-b border-slate-200 bg-white/80 backdrop-blur-md transition-colors dark:border-slate-800 dark:bg-slate-950/80">
      <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
        <div className="flex h-16 items-center justify-between">
          {/* Logo */}
          <div className="flex items-center">
            <Link to="/" className="flex items-center gap-2 text-xl font-bold tracking-tight text-slate-900 dark:text-white group">
              <div className="flex h-9 w-9 items-center justify-center rounded-lg bg-gradient-to-tr from-indigo-500 via-purple-500 to-pink-500 shadow-lg shadow-indigo-500/25 transition-all group-hover:scale-105">
                <Sparkles className="h-5 w-5 text-white" />
              </div>
              <span className="bg-gradient-to-r from-slate-900 via-slate-700 to-indigo-600 dark:from-white dark:via-slate-200 dark:to-indigo-400 bg-clip-text text-transparent transition-all group-hover:opacity-95 font-black">
                MockAI
              </span>
            </Link>
          </div>

          {/* Navigation Links */}
          <div className="hidden md:flex items-center gap-6">
            <Link
              to="/"
              className={`flex items-center gap-2 text-sm font-medium transition-colors hover:text-indigo-600 dark:hover:text-white ${
                isActive("/")
                  ? "text-indigo-600 dark:text-indigo-400 font-semibold"
                  : "text-slate-600 dark:text-slate-400"
              }`}
            >
              <LayoutDashboard className="h-4 w-4" />
              Dashboard
            </Link>
            <Link
              to="/profile"
              className={`flex items-center gap-2 text-sm font-medium transition-colors hover:text-indigo-600 dark:hover:text-white ${
                isActive("/profile")
                  ? "text-indigo-600 dark:text-indigo-400 font-semibold"
                  : "text-slate-600 dark:text-slate-400"
              }`}
            >
              <User className="h-4 w-4" />
              Profile
            </Link>
            <Link
              to="/history"
              className={`flex items-center gap-2 text-sm font-medium transition-colors hover:text-indigo-600 dark:hover:text-white ${
                isActive("/history")
                  ? "text-indigo-600 dark:text-indigo-400 font-semibold"
                  : "text-slate-600 dark:text-slate-400"
              }`}
            >
              <History className="h-4 w-4" />
              History
            </Link>
          </div>

          {/* Actions: Theme Toggle, User Profile, Logout */}
          <div className="flex items-center gap-3">
            <ThemeToggle />

            <div className="flex items-center gap-2 rounded-full bg-slate-100 border border-slate-200 px-3 py-1.5 dark:bg-slate-900 dark:border-slate-800">
              <div className="flex h-6 w-6 items-center justify-center rounded-full bg-indigo-500 text-xs font-bold text-white uppercase shadow-sm">
                {user.name.charAt(0)}
              </div>
              <span className="hidden sm:inline text-xs font-medium text-slate-700 dark:text-slate-300">
                {user.name}
              </span>
            </div>
            
            <button
              onClick={logout}
              className="flex items-center gap-2 rounded-lg border border-slate-200 bg-white px-3 py-1.5 text-xs font-medium text-slate-600 transition-colors hover:bg-slate-100 hover:text-red-600 dark:border-slate-800 dark:bg-slate-950 dark:text-slate-400 dark:hover:bg-slate-900 dark:hover:text-red-400 cursor-pointer shadow-sm"
            >
              <LogOut className="h-3.5 w-3.5" />
              <span className="hidden sm:inline">Logout</span>
            </button>
          </div>
        </div>
      </div>
      
      {/* Mobile Nav Links */}
      <div className="md:hidden flex items-center justify-around border-t border-slate-200 bg-white dark:border-slate-900 dark:bg-slate-950 py-2">
        <Link
          to="/"
          className={`flex flex-col items-center gap-0.5 text-[10px] font-medium transition-colors ${
            isActive("/") ? "text-indigo-600 dark:text-indigo-400" : "text-slate-600 dark:text-slate-400"
          }`}
        >
          <LayoutDashboard className="h-4 w-4" />
          Dashboard
        </Link>
        <Link
          to="/profile"
          className={`flex flex-col items-center gap-0.5 text-[10px] font-medium transition-colors ${
            isActive("/profile") ? "text-indigo-600 dark:text-indigo-400" : "text-slate-600 dark:text-slate-400"
          }`}
        >
          <User className="h-4 w-4" />
          Profile
        </Link>
        <Link
          to="/history"
          className={`flex flex-col items-center gap-0.5 text-[10px] font-medium transition-colors ${
            isActive("/history") ? "text-indigo-600 dark:text-indigo-400" : "text-slate-600 dark:text-slate-400"
          }`}
        >
          <History className="h-4 w-4" />
          History
        </Link>
      </div>
    </nav>
  );
};
export default Navbar;
