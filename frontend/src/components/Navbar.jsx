import { Palette, BrainCircuit } from 'lucide-react';

export default function Navbar({ ThemeToggle }) {
    return (
        <div className="navbar bg-base-100 border-b border-base-300 px-6">
            {/* Left: Brand - Now flexed and centered */}
            <div className="flex-1 flex items-center gap-x-2">
                <BrainCircuit className="text-primary" />
                <span className="text-xl font-bold tracking-wide">
                    Interro
                </span>
            </div>

            {/* Right: Theme toggle */}
            <div className="flex-none">
                <Palette className="cursor-pointer hover:text-primary transition-colors" />
            </div>
        </div>
    );
}