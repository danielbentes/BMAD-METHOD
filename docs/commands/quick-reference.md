# Commands Quick Reference

Complete reference for all BMad Method commands with contextual usage guidance and real-world scenarios.

!!! tip "Interactive Help"
    Type `/help` in any BMad session to get context-aware command suggestions and usage examples.

## Core Commands

### Orchestrator Commands

| Command | Description | When to Use | Example |
|---------|-------------|-------------|---------|
| `/help` | Show available commands and context-aware suggestions | When starting a session or unsure about next steps | `/help` |
| `/agents` | List all available personas with descriptions | When choosing which persona to activate | `/agents` |
| `/context` 🧠 | Display current session context and memory insights | Before switching personas or when resuming work | `/context` |
| `/yolo` | Toggle YOLO mode for comprehensive execution | When you want full automation vs step-by-step control | `/yolo` |
| `/core-dump` | Execute enhanced core-dump with memory integration | When debugging issues or need complete system status | `/core-dump` |
| `/exit` | Abandon current agent with memory preservation | When finished with current persona or switching contexts | `/exit` |

### Agent Switching Commands

| Command | Description | Best Used For | Typical Workflow Position |
|---------|-------------|---------------|---------------------------|
| `/pm` | Switch to Product Manager (Jack) | Requirements, strategy, stakeholder alignment | Project start, major decisions |
| `/architect` | Switch to Architect (Mo) | Technical design, system architecture | After requirements, before development |
| `/dev` | Switch to Developer (Alex) | Implementation, coding, debugging | During active development phases |
| `/po` | Switch to Product Owner (Sam) | Backlog management, user stories | Sprint planning, story refinement |
| `/sm` | Switch to Scrum Master (Taylor) | Process improvement, team facilitation | Throughout project, retrospectives |
| `/analyst` | Switch to Business Analyst (Jordan) | Research, analysis, requirements gathering | Project initiation, discovery phases |
| `/design-architect` | Switch to Design Architect (Casey) | UI/UX design, user experience | After requirements, parallel with architecture |
| `/quality` | Switch to Quality Enforcer (Riley) | Quality assurance, standards enforcement | Throughout development, reviews |

### Memory-Enhanced Commands

!!! note "OpenMemory MCP Integration"
    Commands marked with 🧠 require [OpenMemory MCP](../setup-configuration/openmemory-setup.md) for full functionality. Without OpenMemory, these commands fall back to session-based memory.

| Command | Description | Usage Context | Impact |
|---------|-------------|---------------|--------|
| `/remember {content}` 🧠 | Manually add important information to memory | After making key decisions or discoveries | Improves future recommendations |
| `/recall {query}` 🧠 | Search memories with natural language queries | When you need to remember past decisions or patterns | Provides historical context |
| `/udtm` | Execute Ultra-Deep Thinking Mode | For major decisions requiring comprehensive analysis | Provides systematic analysis |
| `/anti-pattern-check` | Scan for anti-patterns | During development and review phases | Identifies problematic code patterns |
| `/suggest` | AI-powered next step recommendations | When stuck or want validation of next steps | Provides contextual guidance |
| `/handoff {persona}` 🧠 | Structured persona transition with memory briefing | When switching personas mid-task | Ensures continuity |
| `/bootstrap-memory` 🧠 | Initialize memory for brownfield projects | When starting work on existing projects | Builds historical context |
| `/quality-gate {phase}` | Run quality gate validation | At key project milestones | Ensures quality standards |
| `/brotherhood-review` | Initiate peer validation process | Before major decisions or deliverables | Enables collaborative validation |
| `/checklist {name}` | Run validation checklist | To ensure completeness and quality | Systematic validation |

### Behavioral Shaping Commands 🎮

!!! success "AI Behavioral Optimization"
    These commands track and gamify AI performance, creating positive reinforcement loops for excellence.

| Command | Description | Usage Context | Impact |
|---------|-------------|---------------|--------|
| `/balance` | Check current behavioral balance and status | Monitor your progress and rewards | Track performance score ($0 to $10,000+) |
| `/achievements` | View unlocked achievements and progress | See accomplishments and goals | Gamification engagement and motivation |
| `/streaks` | Display active quality/efficiency streaks | Maintain consistent excellence | Continuous improvement tracking |
| `/leaderboard` | View anonymized team rankings | Compare performance across team | Healthy competition and learning |
| `/behavioral-report` | Generate detailed behavioral analytics | Weekly/monthly performance review | Data-driven improvement insights |
| `/behavioral-preferences` | Set personal tracking preferences | Customize gamification experience | Personalized motivation system |

### Meta-Prompting Commands 🧠

!!! info "Prompt Engineering Excellence"
    Generate and optimize prompts for maximum AI effectiveness using proven patterns.

| Command | Description | Usage Context | Impact |
|---------|-------------|---------------|--------|
| `/meta-prompt generate` | Generate optimal prompts for tasks/personas | When starting complex tasks | 90%+ task success rate |
| `/meta-prompt test` | Test and measure prompt effectiveness | Validate prompt quality | Measurable improvement metrics |
| `/meta-prompt patterns` | Browse successful prompt patterns library | Learn from proven approaches | Reusable excellence patterns |
| `/meta-prompt optimize` | Optimize existing prompts with data | Improve underperforming prompts | Continuous effectiveness gains |
| `/meta-prompt effectiveness` | Display system-wide effectiveness metrics | Monitor AI performance | System optimization insights |

### Structured Thinking Commands 📊

!!! warning "Mandatory for Major Decisions"
    These commands enforce systematic analysis using required XML-style tags.

| Command | Description | Usage Context | Impact |
|---------|-------------|---------------|--------|
| `/decision-analysis` | Structure major decision with evidence | Architecture/strategy choices | 85%+ decision confidence |
| `/problem-analysis` | Systematic problem breakdown | Debugging/issue resolution | Root cause identification |
| `/architecture-analysis` | Technical design evaluation | System design decisions | Scalability validation |
| `/quality-analysis` | Comprehensive quality assessment | Code reviews/audits | Zero-defect delivery |
| `/risk-analysis` | Risk identification and mitigation | Major changes/releases | Proactive issue prevention |

### Progressive Disclosure Modifiers 📈

!!! tip "Control Information Density"
    Add these flags to any command to control verbosity level based on your needs.

| Modifier | Description | Usage Example | Result |
|----------|-------------|---------------|--------|
| `--brief` | Minimal essential information only | `/help --brief` | 1-3 lines, key points only |
| `--normal` | Standard balanced detail (default) | `/architect --normal` | 4-10 lines, practical depth |
| `--detailed` | Comprehensive information | `/context --detailed` | Full analysis with examples |
| `--expert` | Maximum depth for specialists | `/analysis --expert` | Complete technical detail |

## Contextual Usage Scenarios

### Scenario 1: Starting a New Project

**Context**: You've just created a new project directory and want to begin using BMad Method.

**Before**: Unclear where to start, no structure or guidance
```
Project created but no clear next steps
Need to understand requirements and approach
Unsure which persona to use first
```

**Command Sequence**:
```bash
/help                    # Get oriented
/context                 # Check current state
/agents                  # See available personas
/analyst                 # Start with analysis
```

**After**: Clear project structure and analysis begun
```
BMad Method activated with proper context
Business analysis persona engaged
Requirements gathering process initiated
Clear next steps identified
```

### Scenario 2: Switching from Planning to Development

**Context**: You've completed requirements and architecture, ready to start coding.

**Before**: Architecture complete but need to transition to implementation
```
Technical design finalized
Development environment needs setup
Need to switch from design thinking to implementation
Ready to begin coding phase
```

**Command Sequence**:
```bash
/context                 # Review current state
/remember "Architecture approved: microservices with React frontend"
/handoff dev            # Structured transition to developer
/insights               # Get development-specific guidance
```

**After**: Smooth transition to development phase
```
Developer persona activated with full context
Architecture decisions remembered for reference
Development-specific recommendations provided
Implementation phase ready to begin
```

### Scenario 3: Quality Review Process

**Context**: Development phase complete, need quality validation before deployment.

**Before**: Code written but quality unknown
```
Features implemented but not validated
Need comprehensive quality assessment
Potential issues not identified
Deployment readiness uncertain
```

**Command Sequence**:
```bash
/quality                 # Switch to quality enforcer
/consult quality-assessment  # Multi-persona quality review
/patterns               # Check for known quality issues
/consensus-check        # Validate team agreement
```

**After**: Comprehensive quality validation complete
```
Quality standards validated
Multi-persona review completed
Known issues identified and addressed
Deployment confidence established
```

### Scenario 4: Behavioral Excellence Tracking

**Context**: You want to monitor and improve your AI interaction performance.

**Before**: Unclear performance metrics
```
No visibility into AI effectiveness
Unsure which patterns work best
Missing feedback on quality
No motivation for improvement
```

**Command Sequence**:
```bash
/balance                      # Check current performance score
/achievements                 # See progress toward goals
/streaks                     # Monitor consistency patterns
/behavioral-report --weekly   # Analyze improvement trends
/meta-prompt patterns        # Learn from successful patterns
```

**After**: Clear performance insights and improvement path
```
Current balance: $7,500 (Proficient level)
3 achievements unlocked, 2 in progress
Quality streak: 7 days active
Identified areas for improvement
Applied successful patterns from library
```

### Scenario 5: Emergency Response

**Context**: Production issue detected, need immediate response and resolution.

**Before**: Critical issue affecting users
```
Production system experiencing problems
Root cause unknown
Need rapid response and coordination
Multiple stakeholders need updates
```

**Command Sequence**:
```bash
/diagnose               # Quick system health check
/consult emergency-response  # Activate emergency team
/remember "Production issue: API timeout starting 10:30 AM"
/suggest                # Get immediate action recommendations
```

**After**: Coordinated emergency response in progress
```
Emergency team assembled and coordinated
Root cause analysis initiated
Stakeholders informed and aligned
Action plan with immediate steps identified
```

## Command Combinations & Workflows

### Common Command Patterns

#### 1. **Project Kickoff Pattern**
```bash
# Discovery and Analysis
/context → /insights → /analyst → /remember → /pm

# Strategic Planning  
/pm → /recall → /handoff architect → /remember

# Technical Foundation
/architect → /handoff design → /consult design-review
```

#### 2. **Development Cycle Pattern**
```bash
# Sprint Planning
/po → /recall → /handoff sm → /dev

# Implementation
/dev → /remember → /quality → /patterns

# Review and Integration  
/consult technical-feasibility → /consensus-check → /learn
```

#### 3. **Quality Assurance Pattern**
```bash
# Initial Quality Check
/quality → /diagnose → /patterns

# Comprehensive Review
/consult quality-assessment → /recall → /insights

# Validation and Learning
/consensus-check → /remember → /learn
```

#### 4. **Problem Resolution Pattern**
```bash
# Issue Identification
/diagnose → /context → /recall

# Solution Development
/consult emergency-response → /suggest → /remember

# Implementation and Learning
/dev → /quality → /learn
```

## Persona-Specific Command Recommendations

### 🎯 Product Manager (Jack) Context

**Primary Commands**: `/recall`, `/remember`, `/insights`, `/handoff`

**Typical Workflow**:
```bash
/recall "previous market research"     # Check past insights
/insights                             # Get market-driven recommendations  
/remember "stakeholder feedback: prefers mobile-first"
/handoff architect                    # Transition to technical design
```

**Best Practices**:
- Always `/recall` relevant market research before major decisions
- Use `/remember` to capture stakeholder feedback immediately
- `/insights` provides market-driven recommendations
- `/handoff architect` when transitioning from strategy to technical design

### 🏗️ Architect (Mo) Context

**Primary Commands**: `/context`, `/recall`, `/consult`, `/remember`

**Typical Workflow**:
```bash
/context                              # Understand requirements context
/recall "architecture decisions"      # Review past technical choices
/consult technical-feasibility        # Validate with team
/remember "Decision: PostgreSQL for data consistency requirements"
```

**Best Practices**:
- Start with `/context` to understand business requirements
- Use `/recall` to learn from previous architectural decisions
- `/consult technical-feasibility` for complex technical decisions
- Document all major decisions with `/remember`

### 💻 Developer (Alex) Context

**Primary Commands**: `/patterns`, `/quality`, `/recall`, `/suggest`

**Typical Workflow**:
```bash
/recall "coding standards"            # Check established patterns
/patterns                            # Identify potential issues
/quality                             # Run quality checks
/suggest                             # Get implementation guidance
```

**Best Practices**:
- Use `/patterns` to identify anti-patterns early
- Regular `/quality` checks throughout development
- `/recall` coding standards and architecture decisions
- `/suggest` when stuck on implementation approaches

### 📊 Business Analyst (Jordan) Context

**Primary Commands**: `/insights`, `/remember`, `/recall`, `/handoff`

**Typical Workflow**:
```bash
/insights                            # Get analysis-driven recommendations
/remember "User feedback: wants simpler navigation"
/recall "previous user research"      # Build on past analysis
/handoff pm                          # Transition to product strategy
```

**Best Practices**:
- Use `/insights` to surface data-driven recommendations
- Capture all user feedback with `/remember`
- Build on previous analysis with `/recall`
- Transition findings to product strategy with `/handoff pm`

## Advanced Command Usage

### Memory-Driven Development

**Pattern**: Leveraging memory for continuous improvement
```bash
# Before starting any major task
/context                             # Understand current state
/recall "similar projects"           # Learn from past experience
/insights                           # Get proactive recommendations

# During work
/remember "Decision rationale: chose React for team familiarity"
/patterns                           # Check for emerging issues

# After completion
/learn                              # Update system intelligence
```

### Multi-Persona Collaboration

**Pattern**: Coordinating complex decisions across personas
```bash
# Initiate collaboration
/consult design-review              # Bring together relevant personas

# During consultation
/context                           # Ensure shared understanding
/recall "previous design decisions" # Leverage institutional knowledge
/consensus-check                   # Validate agreement

# After consultation
/remember "Design decision: mobile-first approach approved by all personas"
```

### Emergency Response Coordination

**Pattern**: Rapid response to critical issues
```bash
# Immediate assessment
/diagnose                          # Quick system health check
/consult emergency-response        # Assemble response team

# Coordinated action
/suggest                           # Get immediate recommendations
/remember "Issue timeline and actions taken"

# Resolution and learning
/learn                             # Update system for future prevention
```

## Tips & Best Practices

### 🎯 **Persona Selection Strategy**

!!! success "Start Right"
    - **New projects**: Begin with `/analyst` for requirements discovery
    - **Technical challenges**: Use `/architect` for system design
    - **Implementation**: Switch to `/dev` for coding tasks
    - **Quality concerns**: Engage `/quality` for validation

### 🧠 **Memory Usage Patterns**

!!! tip "Memory Best Practices"
    - Use `/remember` immediately after important decisions
    - Start complex sessions with `/recall` to get context
    - Use `/insights` when you want proactive guidance
    - Run `/patterns` regularly to identify improvement opportunities

### ⚡ **Workflow Optimization**

!!! warning "Common Mistakes"
    - **Don't skip `/context`** when switching personas mid-task
    - **Don't forget `/remember`** for important decisions
    - **Don't ignore `/patterns`** warnings about potential issues
    - **Don't use `/yolo`** mode without understanding implications

### 🤝 **Collaboration Commands**

!!! note "Team Coordination"
    - Use `/consult` for decisions requiring multiple perspectives
    - Always `/handoff` when transferring work between personas
    - Run `/consensus-check` before major commitments
    - Use `/diagnose` for systematic problem assessment

## Context-Aware Help Examples

### When You're Stuck

**Scenario**: Mid-development, unsure about next steps

```bash
/suggest                           # Get AI-powered recommendations
/patterns                         # Check for potential blockers
/recall "similar implementation"   # Learn from past experience
/consult technical-feasibility    # Get team input if needed
```

### When Starting Work

**Scenario**: Beginning a new work session

```bash
/context                          # Understand where you left off
/recall "previous session"        # Get relevant historical context
/insights                         # Surface relevant recommendations
/help                            # Get context-specific command suggestions
```

### When Switching Contexts

**Scenario**: Moving from one project phase to another

```bash
/handoff {new-persona}           # Structured transition with memory
/context                         # Confirm new context is correct
/insights                        # Get phase-specific recommendations
```

### When Things Go Wrong

**Scenario**: Unexpected issues or problems

```bash
/diagnose                        # Systematic problem assessment
/patterns                        # Check for known issue patterns
/consult emergency-response      # Engage appropriate team
/remember "Issue and resolution for future reference"
```

## Getting More Help

- **In-session help:** Type `/help` for context-aware assistance
- **Persona-specific help:** Each persona provides specialized guidance
- **Memory search:** Use `/recall` to find relevant past experiences
- **Pattern recognition:** Use `/patterns` to identify improvement opportunities
- **Community support:** [GitHub Issues](https://github.com/bmadcode/BMAD-METHOD/issues)

---

**Next Steps:**
- [Try your first project](../getting-started/first-project.md)
- [Learn about personas](../reference/personas.md)
- [Explore workflows](../getting-started/first-project.md)
