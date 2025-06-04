#!/bin/bash

# BMAD Method → Claude Code Command Updater
# Automatically regenerates Claude commands when BMAD registry changes

echo "🔄 BMAD Command Updater"
echo "======================"

# Check if Python is available
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is required but not installed."
    exit 1
fi

# Check if BMAD registry exists
if [ ! -f "bmad-agent/commands/command-registry.yml" ]; then
    echo "❌ BMAD command registry not found: bmad-agent/commands/command-registry.yml"
    exit 1
fi

# Check if generator script exists
if [ ! -f "generate_claude_commands.py" ]; then
    echo "❌ Generator script not found: generate_claude_commands.py"
    exit 1
fi

# Install dependencies if requirements.txt exists
if [ -f "requirements.txt" ]; then
    echo "📦 Installing dependencies..."
    pip3 install -r requirements.txt > /dev/null 2>&1
fi

# Run the command generator
echo "🚀 Generating Claude Code commands from BMAD registry..."
python3 generate_claude_commands.py

# Check if command generation was successful
if [ $? -eq 0 ]; then
    echo "✅ Claude commands generated successfully!"
    
    # Remove README.md from .claude/commands/ as it interferes with Claude Code
    if [ -f ".claude/commands/README.md" ]; then
        echo "🗑️  Removing README.md from .claude/commands/ (Claude Code treats it as a command)"
        rm .claude/commands/README.md
    fi
    
    # Generate comprehensive documentation
    echo "📚 Generating comprehensive documentation..."
    python3 generate_claude_docs.py
    
    if [ $? -eq 0 ]; then
        echo ""
        echo "✅ Complete BMAD→Claude Code integration updated!"
        echo ""
        echo "📁 Available commands:"
        ls -1 .claude/commands/*.md | sed 's|.claude/commands/||' | sed 's|.md|    /project:|'
        echo ""
        echo "💡 Test in Claude Code:"
        echo "   /project:persona architect"
        echo "   /project:quality udtm 'system design'"
        echo "   /project:memory recall 'best practices'"
        echo ""
        echo "📖 Documentation:"
        echo "   docs/claude-code-commands/claude-code-commands-reference.md"
        echo ""
        
        # Optional: Add to git if it's a git repository
        if [ -d ".git" ]; then
            echo "🔀 Adding to git staging area..."
            git add .claude/commands/ docs/claude-code-commands/
            echo "   Use 'git commit' to save changes"
        fi
    else
        echo "⚠️  Commands generated but documentation failed!"
        echo "   Commands are still usable in Claude Code"
    fi
else
    echo "❌ Command generation failed!"
    exit 1
fi 