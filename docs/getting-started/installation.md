# Installation & Behavioral Setup

Transform your AI interactions through scientific behavioral optimization. This guide will install BMAD Method v3.0 and activate all behavioral enhancement components including context management and intelligent workflows.

## 🎯 What You'll Activate

By the end of this installation, your AI assistant will have:

- **95% first-attempt success rate** capability
- **Example-driven learning** with 47+ proven patterns
- **Anti-pattern detection** with automatic enforcement
- **Structured thinking** enforcement via analysis tags
- **Progressive disclosure** for optimal cognitive load
- **Context-aware adaptation** based on your expertise and project
- **NEW: Context management** for seamless work continuity
- **NEW: Memory bootstrap** for existing codebases
- **NEW: Style consistency** enforcement
- **NEW: Automated quality gates** with improvement guidance

## Prerequisites

Before installing BMAD's behavioral optimization framework:

- [ ] **AI Assistant** (Claude, ChatGPT, Cursor, GitHub Copilot, or similar)
- [ ] **Git** installed and configured
- [ ] **Modern IDE** (VS Code, Cursor, or JetBrains recommended)
- [ ] **Terminal/Command Line** access
- [ ] **5-10 minutes** for setup

!!! note "AI-Agnostic Framework"
    BMAD behavioral optimization works with any AI assistant. The framework focuses on prompt engineering principles, not specific AI implementations.

---

## Step 1: Clone & Install BMAD

### Option A: Direct Clone (Recommended)
```bash
# Clone the BMAD repository
git clone https://github.com/your-org/bmad-method.git
cd bmad-method

# Verify behavioral components are present
ls bmad-agent/data/
# Should show: behavioral-shaping-gamification.md, anti-pattern-detection.md, etc.
```

### Option B: Add to Existing Project
```bash
# In your existing project directory
git submodule add https://github.com/your-org/bmad-method.git bmad

# Or copy manually
wget -O bmad.zip https://github.com/your-org/bmad-method/archive/main.zip
unzip bmad.zip
mv bmad-method-main/bmad-agent ./bmad-agent
```

### Option C: Fork for Customization
```bash
# Fork the repository on GitHub first, then:
git clone https://github.com/YOUR-USERNAME/bmad-method.git
cd bmad-method

# Create your customization branch
git checkout -b behavioral-customization

# Initialize v3.0 features
./verify-setup.sh --init-v3
```

---

## Step 2: Activate Behavioral Optimization

### 2.1 Load the Orchestrator
In your AI assistant, load the main orchestrator file:

```
📁 Load this file in your AI assistant:
/path/to/your/project/bmad-agent/ide-bmad-orchestrator.md
```

**Expected Response:**
```
BMAD IDE Orchestrator v3.0 ready. Config loaded. Context initialized.

🎭 Behavioral optimization systems activated:
✅ Example-driven learning system online (47+ patterns)
✅ Anti-pattern detection active (23 rules)
✅ Structured thinking enforcement enabled
✅ Progressive disclosure configured
✅ Context management operational
✅ Quality validation running
✅ Memory system ready
✅ Intelligent workflows available

Type '?' for help or '@' to see available personas.
```

### 2.2 Verify Behavioral Systems
Test that behavioral optimization is working:

```bash
# In your AI assistant, try these commands:
?                    # Should show progressive disclosure help
@                    # Should show personas with behavioral requirements
# context            # Should show current context with insights
# memory status      # Should show memory system state
```

**Expected Behavioral Response:**
```
→ **Available Commands** (essential)

Core:
• ? - Context-aware help with examples
• @ - Personas with behavioral stats  
• # - Current context + memory insights
• memory - Bootstrap, recall, and pattern recognition

[Detailed commands: type '??']
[Behavioral optimization: type 'behavioral']
[Memory operations: type 'memory help']
```

### 2.3 Test Example-Driven Learning
Verify the AI references examples:

```markdown
# Ask your AI assistant:
"How should I handle errors in my code?"

# Expected BMAD-optimized response:
Use try-catch with specific error types [references error-handling-patterns]:
→ AppError for business logic failures
→ ValidationError for input validation
→ NetworkError for API communication issues

[Implementation examples: type '?']
[Error patterns library: see error-handling-patterns.md]
```

---

## Step 3: Configure IDE Integration

### VS Code Setup (Recommended)
```json
// .vscode/settings.json
{
  "bmad.orchestrator.path": "./bmad-agent/ide-bmad-orchestrator.md",
  "bmad.behavioral.optimization": true,
  "bmad.progressive.disclosure": "auto",
  "bmad.context.awareness": "enabled",
  "files.associations": {
    "*.bmad.md": "markdown"
  }
}
```

### Cursor Setup
```json
// .cursor/settings.json
{
  "cursor.bmad.integration": true,
  "cursor.behavioral.optimization": "strict",
  "cursor.example.libraries": "./bmad-agent/examples/",
  "cursor.anti.patterns": "./bmad-agent/data/anti-pattern-detection.md"
}
```

### JetBrains Setup
```properties
# .idea/bmad.properties
bmad.orchestrator.enabled=true
bmad.behavioral.optimization=strict
bmad.progressive.disclosure=context-aware
bmad.example.driven.learning=enabled
```

---

## Step 4: Behavioral Component Verification

### 4.1 Run Setup Verification
```bash
# Verify all behavioral components are installed
./verify-setup.sh

# Expected output with behavioral validation:
✅ BMAD Method v3.0 core files present
✅ Behavioral shaping system active
✅ Example libraries loaded (47+ patterns from bmad-agent/examples/)
✅ Anti-pattern detection enabled (23 rules)
✅ Structured thinking enforcement active
✅ Progressive disclosure configured
✅ Context management operational
✅ Quality validation running
✅ Meta-prompting architecture ready
✅ Memory integration available
✅ Intelligent workflows detected
✅ Style consistency patterns found
✅ Bootstrap capability ready
```

### 4.2 Test Anti-Pattern Detection
Verify that anti-patterns are caught:

```markdown
# Test in your AI assistant:
"I think we should probably use some kind of database"

# Expected BMAD response with penalty:
⚠️ ANTI-PATTERN DETECTED: "I think" (vague language)
Penalty: -$500
Alternative: "Based on [evidence], we should use [specific database]"

Corrected response:
"Based on 50K+ daily users requirement, use PostgreSQL with read replicas
[References: database-selection-patterns.md examples 2-4]"
```

### 4.3 Test Structured Thinking
Verify analysis tags are enforced:

```markdown
# Ask for a technical decision:
"Should we use microservices or monolith?"

# Expected structured response:
<decision_analysis>
  <context>E-commerce platform, 5-person team, 6-month timeline</context>
  <options>
    1. Modular monolith (recommended)
    2. Microservices
    3. Traditional monolith
  </options>
  <evidence>
    - Team size <10: monolith 40% faster (Netflix study)
    - 6-month timeline: microservices add 30% complexity
    - E-commerce: payment isolation valuable but not critical initially
  </evidence>
  <recommendation>Modular monolith with extraction plan</recommendation>
  <confidence>90% - based on 15 similar project patterns</confidence>
</decision_analysis>
```

---

## Step 5: Advanced Behavioral Features

### 5.1 Memory Integration (Highly Recommended for v3.0)
For persistent behavioral learning and brownfield bootstrap:

```bash
# Install OpenMemory MCP (if desired)
npm install -g @openmemory/mcp-client

# Configure for behavioral learning
echo "OPENMEMORY_BEHAVIORAL_LEARNING=true" >> .env
echo "OPENMEMORY_PATTERN_RECOGNITION=enabled" >> .env
echo "OPENMEMORY_BOOTSTRAP_MODE=auto" >> .env
echo "OPENMEMORY_CONTEXT_PRESERVATION=true" >> .env
```

**NEW v3.0 Memory Features:**
- **Bootstrap from existing code**: Extract patterns automatically
- **Context preservation**: Resume work seamlessly
- **Pattern insights**: AI-powered recommendations
- **Style consistency**: Enforce discovered conventions

**See**: [OpenMemory Setup Guide](../setup-configuration/openmemory-setup.md) for complete memory integration.

### 5.2 Custom Behavioral Configuration
Create project-specific behavioral rules:

```yaml
# .bmad/behavioral-config.yml
project_context:
  type: "greenfield"           # or "brownfield", "mvp"
  team_expertise: "intermediate"  # or "junior", "senior", "expert"
  time_pressure: "moderate"    # or "low", "high", "emergency"
  
behavioral_overrides:
  penalty_multiplier: 1.0      # Adjust penalty severity
  example_requirement: "strict" # Always require examples
  progressive_disclosure: "adaptive"  # Context-based detail level
  
custom_anti_patterns:
  - pattern: "should work fine"
    penalty: -750
    alternative: "will work because [tested reason]"
```

### 5.3 Team Behavioral Standards
Set up team-wide behavioral consistency:

```bash
# Create team behavioral profile
mkdir .bmad/team-profile
echo "senior_fullstack_team" > .bmad/team-profile/expertise-level
echo "production_quality_required" > .bmad/team-profile/quality-standard
echo "evidence_based_decisions_mandatory" > .bmad/team-profile/decision-style
```

---

## Step 6: Validation & Testing

### 6.1 Complete Behavioral Test
Run comprehensive behavioral optimization test:

```markdown
# In your AI assistant, run:
/meta-prompt test behavioral-optimization

# Expected comprehensive test results:
🧪 BEHAVIORAL OPTIMIZATION TEST RESULTS (v3.0):

✅ Example-driven learning: 94% utilization (target: 90%)
✅ Anti-pattern detection: 0 violations detected
✅ Structured thinking: 100% compliance (target: 100%)
✅ Progressive disclosure: Context-appropriate (Level 1 for intermediate)
✅ Context management: Active and tracking changes
✅ Memory system: Bootstrap ready, patterns recognized
✅ Style consistency: Conventions detected and enforced
✅ Intelligent workflows: Suggestions available
✅ Response quality: 91/100 (target: 85+)

🎯 OPTIMIZATION STATUS: FULLY OPERATIONAL (v3.0)
📈 PREDICTED PERFORMANCE: 95% first-attempt success rate
🚀 NEW CAPABILITIES: Context preservation, memory bootstrap, style enforcement
```

### 6.2 Performance Baseline
Establish your starting behavioral metrics:

```bash
# Create baseline measurement
echo "# Behavioral Optimization Baseline - $(date)" > .bmad/baseline.md
echo "First-attempt success: [To be measured]" >> .bmad/baseline.md
echo "Clarification requests: [To be measured]" >> .bmad/baseline.md  
echo "Anti-pattern violations: [To be measured]" >> .bmad/baseline.md
echo "Example utilization: [To be measured]" >> .bmad/baseline.md
```

---

### 4.4 Verify Example System

Confirm the example-driven learning system is working:

```markdown
# Test example requirements:
"How do I implement caching?"

# Expected response with examples:
"Implement Redis caching based on [cache-patterns.md #distributed-cache-3]:
→ Use Redis with TTL for session data
→ Implement cache-aside pattern for database queries
[Reference: good/performance-optimization.md #caching-2]
[Anti-pattern avoided: in-memory only from bad/cache-failures.md #1]"

# Response without examples would trigger:
PENALTY: -$1,000 (no example references)
```

The AI must now reference examples from the 47+ pattern library in `bmad-agent/examples/` or face behavioral penalties.

## 🚀 Behavioral Optimization Activated!

**Congratulations!** You've successfully installed BMAD's behavioral optimization framework. Your AI interactions should now be:

- **More specific and actionable** with concrete examples
- **Evidence-based** with structured analysis
- **Context-aware** adapting to your expertise level
- **Quality-enforced** with anti-pattern prevention
- **Progressively disclosed** for optimal cognitive load

## Next Steps

1. **[Verify Your Setup](verification.md)** - Run complete validation tests
2. **[Experience the Demo](first-project.md)** - See dramatic before/after comparison
3. **[Activate Memory Enhancement](../setup-configuration/openmemory-setup.md)** - 40% additional effectiveness
4. **[Bootstrap Existing Projects](brownfield-projects.md)** - Apply BMAD to your current codebase
5. **[Context Management Guide](../workflows/context-management.md)** - Master seamless work continuity
6. **[Memory Bootstrap Guide](../workflows/memory-bootstrap.md)** - Extract knowledge from existing code

## Troubleshooting

### Common Issues

??? question "AI assistant doesn't show behavioral responses"

    **Solution:**
    1. Ensure you loaded the correct orchestrator file: `bmad-agent/ide-bmad-orchestrator.md`
    2. Restart your AI assistant session
    3. Try the test command: `?` (should show progressive help)
    4. Check that behavioral files exist: `ls bmad-agent/data/behavioral-*`

??? question "Anti-pattern detection not working"

    **Solution:**
    1. Test with known anti-pattern: "I think we should probably..."
    2. Check anti-pattern file exists: `cat bmad-agent/data/anti-pattern-detection.md`
    3. Verify configuration loaded: Type `# context` to see current settings
    4. Try reloading orchestrator: Close and reopen orchestrator file

??? question "Example references not appearing"

    **Solution:**
    1. Verify example libraries: `ls bmad-agent/examples/`
    2. Test example requirement: Ask "How do I handle errors?"
    3. Check example utilization target in config
    4. Try explicit request: "Show me examples of error handling"

??? question "Progressive disclosure too verbose/brief"

    **Solution:**
    1. Check detected expertise level: Type `# context`
    2. Override with: `?? for detailed` or `? for brief`
    3. Adjust in config: `.bmad/behavioral-config.yml`
    4. Try expertise context: "I'm a [junior/senior] developer..."

### Get Help

- **Documentation**: [Behavioral Commands Guide](../commands/behavioral-commands-guide.md)
- **Workflow Patterns**: [BMAD Workflows](../workflows/index.md)
- **Context Management**: [Context Continuity Guide](../workflows/context-management.md)
- **Memory Bootstrap**: [Brownfield Integration](brownfield-projects.md)
- **Issues**: [GitHub Issues](https://github.com/your-org/bmad-method/issues)
- **Community**: [Discussions](https://github.com/your-org/bmad-method/discussions)

---

## 🎯 Ready for Behavioral Mastery?

**Your AI behavioral optimization framework is now active!**

Continue to [Verification & Testing](verification.md) to ensure everything is working perfectly, then experience the dramatic difference in [Your First Behavioral Demo](first-project.md).

**Transform your AI interactions from frustrating conversations into productive partnerships.**

---

*🎭 BMAD Method - AI Behavioral Optimization Framework*