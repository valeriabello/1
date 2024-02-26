import { create } from 'zustand';
import { persist } from 'zustand/middleware'

interface DarkModeStore {
  darkMode: boolean;
  toggleDarkMode: () => void;
}

export const useDarkMode = create<DarkModeStore>()(
  persist(
    (set) => ({
      darkMode: false, //cambiar a true para q inicie en DARKMODE
      toggleDarkMode: () => set((state) => ({ darkMode: !state.darkMode })),
    }),
    {
      name: 'theme', 
    }
  )
)