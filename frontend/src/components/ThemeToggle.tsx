import React from "react";
import { Sun, Moon } from "lucide-react";
import { useTheme } from "./theme-provider";

interface ThemeToggleProps {
  className?: string;
  showLabel?: boolean;
}

export const ThemeToggle: React.FC<ThemeToggleProps> = ({ className = "", showLabel = false }) => {
  const { theme, setTheme } = useTheme();

  // Determine if effectively in dark mode
  const isDark =
    theme === "dark" ||
    (theme === "system" &&
      typeof window !== "undefined" &&
      window.matchMedia("(prefers-color-scheme: dark)").matches);

  const toggleTheme = () => {
    setTheme(isDark ? "light" : "dark");
  };

  return (
    <button
      type="button"
      onClick={toggleTheme}
      aria-label={isDark ? "Switch to white background (Light mode)" : "Switch to black background (Dark mode)"}
      title={isDark ? "Switch to white background (Light mode)" : "Switch to black background (Dark mode)"}
      className={`group relative flex items-center gap-2 rounded-xl border border-slate-200 bg-white/80 p-2 text-slate-700 shadow-sm backdrop-blur-md transition-all hover:bg-slate-100 hover:text-slate-900 active:scale-95 dark:border-slate-800 dark:bg-slate-900/80 dark:text-slate-300 dark:hover:bg-slate-800 dark:hover:text-white cursor-pointer ${className}`}
    >
      <div className="relative h-5 w-5 flex items-center justify-center">
        <Sun
          className={`h-4 w-4 text-amber-500 transition-all duration-300 ${
            isDark
              ? "scale-0 rotate-90 opacity-0 absolute"
              : "scale-100 rotate-0 opacity-100"
          }`}
        />
        <Moon
          className={`h-4 w-4 text-indigo-400 transition-all duration-300 ${
            isDark
              ? "scale-100 rotate-0 opacity-100"
              : "scale-0 -rotate-90 opacity-0 absolute"
          }`}
        />
      </div>

      {showLabel && (
        <span className="text-xs font-medium">
          {isDark ? "Light Mode" : "Dark Mode"}
        </span>
      )}
    </button>
  );
};

export default ThemeToggle;
