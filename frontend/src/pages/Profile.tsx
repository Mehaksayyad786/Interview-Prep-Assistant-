import React, { useState, useEffect } from "react";
import { useAuth } from "../context/AuthContext";
import { Sparkles, User, Briefcase, GraduationCap, Code, Plus, X, Save } from "lucide-react";

const TARGET_ROLES = [
  "Python Developer",
  "Java Developer",
  "Data Analyst",
  "Data Scientist",
  "Machine Learning Engineer",
  "AI Engineer",
];

const EXPERIENCE_LEVELS = ["Fresher", "Mid-Level", "Senior"];

export const Profile: React.FC = () => {
  const { user, updateProfile } = useAuth();
  
  // Form states
  const [name, setName] = useState<string>("");
  const [education, setEducation] = useState<string>("");
  const [skills, setSkills] = useState<string[]>([]);
  const [experienceLevel, setExperienceLevel] = useState<string>("");
  const [preferredRole, setPreferredRole] = useState<string>("");
  
  // Custom skill input state
  const [skillInput, setSkillInput] = useState<string>("");
  
  // Message states
  const [message, setMessage] = useState<{ type: "success" | "error"; text: string } | null>(null);
  const [saving, setSaving] = useState<boolean>(false);

  // Sync state with user profile
  useEffect(() => {
    if (user) {
      setName(user.name || "");
      setEducation(user.education || "");
      setSkills(user.skills || []);
      setExperienceLevel(user.experience_level || EXPERIENCE_LEVELS[0]);
      setPreferredRole(user.preferred_job_role || TARGET_ROLES[0]);
    }
  }, [user]);

  const handleAddSkill = (e: React.FormEvent) => {
    e.preventDefault();
    const cleanSkill = skillInput.trim();
    if (cleanSkill && !skills.includes(cleanSkill)) {
      setSkills([...skills, cleanSkill]);
      setSkillInput("");
    }
  };

  const handleRemoveSkill = (skillToRemove: string) => {
    setSkills(skills.filter((s) => s !== skillToRemove));
  };

  const handleSave = async (e: React.FormEvent) => {
    e.preventDefault();
    setMessage(null);
    setSaving(true);

    try {
      const result = await updateProfile({
        name,
        education,
        skills,
        experience_level: experienceLevel,
        preferred_job_role: preferredRole,
      });

      if (result.success) {
        setMessage({ type: "success", text: "Profile updated successfully!" });
      } else {
        setMessage({ type: "error", text: result.error || "Failed to save profile." });
      }
    } catch (err) {
      setMessage({ type: "error", text: "Something went wrong. Please check your connection." });
    } finally {
      setSaving(false);
    }
  };

  return (
    <div className="mx-auto max-w-4xl px-4 py-8 sm:px-6 lg:px-8">
      {/* Header */}
      <div className="mb-8 flex items-center justify-between">
        <div>
          <h1 className="text-3xl font-bold tracking-tight text-slate-900 dark:text-white flex items-center gap-2">
            <User className="h-7 w-7 text-indigo-500" />
            Candidate Profile
          </h1>
          <p className="mt-2 text-sm text-slate-600 dark:text-slate-400">
            Set up your profile details. They will be used to customize your mock interview questions.
          </p>
        </div>
      </div>

      {/* Profile Form */}
      <form onSubmit={handleSave} className="space-y-6">
        <div className="rounded-2xl border border-slate-200 bg-white p-6 md:p-8 shadow-sm dark:border-slate-800 dark:bg-slate-900/60 dark:shadow-xl backdrop-blur-xl space-y-6">
          
          {/* Status Message */}
          {message && (
            <div
              className={`rounded-lg border p-4 text-sm ${
                message.type === "success"
                  ? "border-green-500/30 bg-green-500/10 text-green-600 dark:text-green-400"
                  : "border-red-500/30 bg-red-500/10 text-red-600 dark:text-red-400"
              }`}
            >
              {message.text}
            </div>
          )}

          {/* Personal Info Grid */}
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div className="space-y-1.5">
              <label className="text-xs font-semibold text-slate-700 dark:text-slate-300 flex items-center gap-1.5" htmlFor="name">
                <User className="h-3.5 w-3.5 text-indigo-500" />
                Full Name
              </label>
              <input
                id="name"
                type="text"
                required
                value={name}
                onChange={(e) => setName(e.target.value)}
                placeholder="Mehak"
                className="block w-full rounded-lg border border-slate-200 bg-slate-50 py-2.5 px-3 text-sm text-slate-900 placeholder-slate-400 outline-none transition-all focus:border-indigo-500 focus:ring-1 focus:ring-indigo-500 focus:bg-white dark:border-slate-800 dark:bg-slate-950/50 dark:text-white dark:placeholder-slate-500 dark:focus:bg-slate-950"
              />
            </div>

            <div className="space-y-1.5">
              <label className="text-xs font-semibold text-slate-700 dark:text-slate-300 flex items-center gap-1.5" htmlFor="education">
                <GraduationCap className="h-3.5 w-3.5 text-indigo-500" />
                Education
              </label>
              <input
                id="education"
                type="text"
                value={education}
                onChange={(e) => setEducation(e.target.value)}
                placeholder="B.Tech CSE (AI & DS)"
                className="block w-full rounded-lg border border-slate-200 bg-slate-50 py-2.5 px-3 text-sm text-slate-900 placeholder-slate-400 outline-none transition-all focus:border-indigo-500 focus:ring-1 focus:ring-indigo-500 focus:bg-white dark:border-slate-800 dark:bg-slate-950/50 dark:text-white dark:placeholder-slate-500 dark:focus:bg-slate-950"
              />
            </div>
          </div>

          {/* Settings Grid */}
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div className="space-y-1.5">
              <label className="text-xs font-semibold text-slate-700 dark:text-slate-300 flex items-center gap-1.5" htmlFor="experience">
                <Briefcase className="h-3.5 w-3.5 text-indigo-500" />
                Experience Level
              </label>
              <select
                id="experience"
                value={experienceLevel}
                onChange={(e) => setExperienceLevel(e.target.value)}
                className="block w-full rounded-lg border border-slate-200 bg-slate-50 py-2.5 px-3 text-sm text-slate-900 outline-none transition-all focus:border-indigo-500 focus:ring-1 focus:ring-indigo-500 focus:bg-white dark:border-slate-800 dark:bg-slate-950 dark:text-white cursor-pointer"
              >
                {EXPERIENCE_LEVELS.map((lvl) => (
                  <option key={lvl} value={lvl} className="bg-white text-slate-900 dark:bg-slate-950 dark:text-white">
                    {lvl}
                  </option>
                ))}
              </select>
            </div>

            <div className="space-y-1.5">
              <label className="text-xs font-semibold text-slate-700 dark:text-slate-300 flex items-center gap-1.5" htmlFor="targetRole">
                <Sparkles className="h-3.5 w-3.5 text-indigo-500" />
                Target Role
              </label>
              <select
                id="targetRole"
                value={preferredRole}
                onChange={(e) => setPreferredRole(e.target.value)}
                className="block w-full rounded-lg border border-slate-200 bg-slate-50 py-2.5 px-3 text-sm text-slate-900 outline-none transition-all focus:border-indigo-500 focus:ring-1 focus:ring-indigo-500 focus:bg-white dark:border-slate-800 dark:bg-slate-950 dark:text-white cursor-pointer"
              >
                {TARGET_ROLES.map((role) => (
                  <option key={role} value={role} className="bg-white text-slate-900 dark:bg-slate-950 dark:text-white">
                    {role}
                  </option>
                ))}
              </select>
            </div>
          </div>

          {/* Skills Management */}
          <div className="space-y-3 pt-2">
            <label className="text-xs font-semibold text-slate-700 dark:text-slate-300 flex items-center gap-1.5">
              <Code className="h-3.5 w-3.5 text-indigo-500" />
              Skills & Technologies
            </label>

            {/* Input field */}
            <div className="flex gap-2">
              <input
                type="text"
                value={skillInput}
                onChange={(e) => setSkillInput(e.target.value)}
                placeholder="Python, SQL, Machine Learning..."
                className="block flex-1 rounded-lg border border-slate-200 bg-slate-50 py-2.5 px-3 text-sm text-slate-900 placeholder-slate-400 outline-none transition-all focus:border-indigo-500 focus:ring-1 focus:ring-indigo-500 focus:bg-white dark:border-slate-800 dark:bg-slate-950/50 dark:text-white dark:placeholder-slate-500 dark:focus:bg-slate-950"
                onKeyDown={(e) => {
                  if (e.key === "Enter") {
                    e.preventDefault();
                    handleAddSkill(e);
                  }
                }}
              />
              <button
                type="button"
                onClick={handleAddSkill}
                className="flex h-10 w-10 items-center justify-center rounded-lg bg-indigo-600 text-white shadow-md shadow-indigo-600/10 hover:bg-indigo-500 active:scale-[0.95] transition-all cursor-pointer"
              >
                <Plus className="h-5 w-5" />
              </button>
            </div>

            {/* Tag container */}
            <div className="flex flex-wrap gap-2 pt-2">
              {skills.length === 0 ? (
                <span className="text-xs text-slate-500 italic">No skills added yet. Add skills to help evaluate questions.</span>
              ) : (
                skills.map((skill) => (
                  <div
                    key={skill}
                    className="flex items-center gap-1.5 rounded-full border border-indigo-500/30 bg-indigo-500/10 px-3 py-1 text-xs font-medium text-indigo-700 dark:text-indigo-300 transition-colors hover:bg-indigo-500/20"
                  >
                    <span>{skill}</span>
                    <button
                      type="button"
                      onClick={() => handleRemoveSkill(skill)}
                      className="text-indigo-500 hover:text-indigo-700 dark:text-indigo-400 dark:hover:text-indigo-200 cursor-pointer"
                    >
                      <X className="h-3.5 w-3.5" />
                    </button>
                  </div>
                ))
              )}
            </div>
          </div>
        </div>

        {/* Submit */}
        <div className="flex justify-end">
          <button
            type="submit"
            disabled={saving}
            className="flex items-center gap-2 rounded-lg bg-indigo-600 px-6 py-3 text-sm font-semibold text-white shadow-lg shadow-indigo-500/10 hover:bg-indigo-500 active:scale-[0.98] transition-all disabled:opacity-50 cursor-pointer"
          >
            {saving ? (
              <div className="h-4 w-4 animate-spin rounded-full border-2 border-white border-t-transparent" />
            ) : (
              <>
                <Save className="h-4 w-4" />
                Save Changes
              </>
            )}
          </button>
        </div>
      </form>
    </div>
  );
};
export default Profile;
