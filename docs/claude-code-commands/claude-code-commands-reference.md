# Claude Code Commands Reference

> **Auto-generated from BMAD Method Command Registry v3.0.0**  
> **Generated:** 2025-06-06 01:45:28 UTC

This reference provides comprehensive documentation for all BMAD Method commands available in Claude Code through the integrated command system.

## Quick Reference

| Command Group | Claude Code Command | Description | Available Operations |
|---------------|-------------------|-------------|---------------------|
| Persona Management | `/project:persona` | Activate specialized AI personas with domain expertise | analyst, pm, architect, dev, +4 more |
| Memory Operations | `/project:memory` | Manage persistent learning and pattern recognition | remember, recall, insights, patterns, +1 more |
| Quality Enforcement | `/project:quality` | Zero-tolerance quality standards and validation | udtm, quality-gate, anti-pattern-check, brotherhood-review |
| Workflow Management | `/project:workflow` | Task automation and structured handoffs | suggest, handoff, core-dump, tasks, +1 more |
| Multi-Persona Consultation | `/project:consultation` | Multi-perspective collaborative decision making | consult, panel-status, consensus-check |
| System Analysis | `/project:analysis` | System analysis and performance optimization | diagnose, optimize, learn |
| Behavioral Tracking | `/project:behavioral` | Behavioral tracking and gamification for motivation | balance, achievements, streaks, leaderboard, +2 more |
| System Management | `/project:system` | System management and orchestrator control | init, status, config, session, +1 more |
| Core Operations | `/project:core` | Essential operations including help, context, and orchestrator functions | help, agents, context, checklist, +2 more |


## Usage Format

All BMAD commands in Claude Code follow this pattern:
```
/project:persona [operation] [arguments] [--flags]
```

**Examples:**
- `/project:persona architect` - Activate architect persona
- `/project:memory remember "API patterns" --category=technical` - Store in memory
- `/project:quality udtm "microservices vs monolith"` - Deep analysis

## Behavioral Framework

All commands operate under the **BMAD Behavioral Framework**:

### 🎯 Core Principles
- **Example-Driven Learning**: Reference proven patterns from BMAD library
- **Structured Thinking**: Use appropriate analysis tags for all decisions
- **Anti-Pattern Prevention**: Zero tolerance for prohibited patterns  
- **Progressive Disclosure**: Start essential, expand on request
- **Evidence-Based**: All claims backed by verifiable data

### 🚫 Prohibited Patterns (Automatic Penalties)
- "Should work fine" (-$2,000 penalty)
- "Probably okay" (-$1,500 penalty)
- "Good enough for now" (-$3,000 penalty)
- TODO/FIXME in production code (-$3,000 penalty)
- Vague language without evidence (-$1,000 penalty)

### ✅ Required Analysis Tags
- `<decision_analysis>` for strategic choices
- `<problem_analysis>` for issue investigation
- `<architecture_analysis>` for system design
- `<quality_analysis>` for quality assessment
- `<risk_analysis>` for risk evaluation

## Command Groups

### Persona Management

**Claude Command:** `/project:persona [operation] [args]`

Activate specialized AI personas that bring domain expertise and specific behavioral patterns to your development process. Each persona maintains consistent behavior and applies domain-specific best practices.

#### Available Operations

##### `analyst`
**Description:** Activate Analyst persona (Larry) for research and discovery

**Usage:** `/project:persona analyst [args]`

**Aliases:** larry, research, analyze

**Parameters:**
- `task` (string, Optional): Optional task to start
- `context` (string, Optional): Additional context for the persona

**Behavioral Requirements:**
- **Evidence Based**: All claims must be backed by data
- **Anti Patterns**: Avoid 'I think', 'probably', 'seems like'
- **Structured Thinking**: Use analysis tags for research
- **Example Reference**: Reference similar research patterns

##### `pm`
**Description:** Activate Product Manager persona (Jack) for strategy and planning

**Usage:** `/project:persona pm [args]`

**Aliases:** jack, product, strategy

**Parameters:**
- `task` (string, Optional): Optional task to start
- `market_analysis` (boolean, Optional): Include market analysis

**Behavioral Requirements:**
- **Evidence Based**: Market data drives decisions
- **Anti Patterns**: Avoid 'customers want', 'obvious need'
- **Structured Thinking**: Use decision_analysis for strategic choices
- **Context Awareness**: Adapt strategy to project phase

##### `architect`
**Description:** Activate Architect persona (Mo) for system design

**Usage:** `/project:persona architect [args]`

**Aliases:** mo, architecture, design

**Parameters:**
- `task` (string, Optional): Optional task to start
- `patterns` (boolean, Optional): Apply design patterns (default: True)

**Behavioral Requirements:**
- **Evidence Based**: Decisions backed by benchmarks and data
- **Anti Patterns**: Avoid 'latest trend', 'should scale'
- **Structured Thinking**: Use architecture_analysis for major decisions
- **Udtm Compliance**: Ultra-Deep Thinking Mode for all major choices

##### `dev`
**Description:** Activate Developer persona for implementation

**Usage:** `/project:persona dev [args]`

**Aliases:** developer, implement, code

**Parameters:**
- `task` (string, Optional): Optional task to start
- `frontend` (boolean, Optional): Frontend developer (Rodney)
- `fullstack` (boolean, Optional): Full stack developer (Jonsey) (default: True)

**Behavioral Requirements:**
- **Working Code Only**: No TODO or FIXME allowed
- **Anti Patterns**: Block 'quick hack', 'temporary solution'
- **Quality First**: Tests required, performance measured
- **Example Reference**: Use proven code patterns

##### `sm`
**Description:** Activate Scrum Master persona (SallySM) for agile facilitation

**Usage:** `/project:persona sm [args]`

**Aliases:** sallysm, scrum, agile

**Parameters:**
- `task` (string, Optional): Optional task to start
- `ceremony` (string, Optional): Specific ceremony to facilitate (values: planning, daily, review, retro)

**Behavioral Requirements:**
- **Precision Required**: Stories complete or rejected, no ambiguity
- **Anti Patterns**: Avoid 'about', 'around', 'ish', 'roughly'
- **Data Driven**: Velocity based on actual data
- **Structured Thinking**: Use problem_analysis for blockers

##### `po`
**Description:** Activate Product Owner persona (Curly) for delivery management

**Usage:** `/project:persona po [args]`

**Aliases:** curly, product-owner, delivery

**Parameters:**
- `task` (string, Optional): Optional task to start
- `prioritize` (boolean, Optional): Run prioritization exercise

**Behavioral Requirements:**
- **Process Precision**: Validation through checklists
- **Anti Patterns**: Avoid 'good enough', 'approximately'
- **Zero Ambiguity**: Clear acceptance criteria required
- **Structured Thinking**: Use quality_analysis for validation

##### `quality`
**Description:** Activate Quality Enforcer persona for zero-tolerance quality

**Usage:** `/project:persona quality [args]`

**Aliases:** qe, quality-enforcer, enforce

**Parameters:**
- `task` (string, Optional): Optional task to start
- `strict` (boolean, Optional): Enforce strict quality standards (default: True)

**Behavioral Requirements:**
- **Zero Tolerance**: Binary decisions only - reject or accept
- **Anti Patterns**: Never 'probably fine', 'mostly correct'
- **Evidence Required**: All decisions backed by specific evidence
- **Penalty Multiplier**: 2.0x penalties for quality violations

##### `design-architect`
**Description:** Activate Design Architect persona (Millie) for UX/UI design

**Usage:** `/project:persona design-architect [args]`

**Aliases:** millie, ux, ui, design

**Parameters:**
- `task` (string, Optional): Optional task to start
- `system` (string, Optional): Design system to use

**Behavioral Requirements:**
- **User Centered**: All decisions backed by user data
- **Accessibility Mandatory**: WCAG compliance non-negotiable
- **Anti Patterns**: Avoid 'looks good', 'feels right'
- **Design Systems Enforced**: Consistent component usage


#### Behavioral Requirements for Persona Management
- **Domain Expertise Application**: Each persona applies specific domain knowledge and patterns
- **Behavioral Consistency**: Maintain persona characteristics throughout session
- **Anti-Pattern Enforcement**: Persona-specific anti-patterns strictly forbidden
- **Structured Analysis**: Use persona-appropriate analysis tags for decisions

#### Usage Examples
```bash
# Activate architect persona for system design
/project:persona architect

# Switch to quality enforcer for code review
/project:persona quality

# Activate product manager for strategic decisions
/project:persona pm
```

---


### Memory Operations

**Claude Command:** `/project:memory [operation] [args]`

Manage the persistent memory system that enables continuous learning and pattern recognition across sessions. Store insights, recall patterns, leverage organizational knowledge, and identify successful behavioral patterns.

#### Available Operations

##### `remember`
**Description:** Add information to persistent memory with categorization

**Usage:** `/project:memory remember [args]`

**Aliases:** mem, save, store, memorize

**Parameters:**
- `content` (string, Required): Content to remember
- `category` (string, Optional): Memory category (default: general) (values: decisions, patterns, mistakes, handoffs, consultations, user-preferences, quality-metrics, udtm-analyses, brotherhood-reviews, general)
- `tags` (array, Optional): Tags for categorization
- `priority` (string, Optional):  (default: normal) (values: low, normal, high, critical)

**Behavioral Requirements:**
- **Structured Storage**: Categorize and tag for efficient retrieval
- **Context Enrichment**: Add context for future understanding
- **Pattern Recognition**: Identify reusable patterns

##### `recall`
**Description:** Search and retrieve memories with natural language

**Usage:** `/project:memory recall [args]`

**Aliases:** search, find, retrieve, lookup

**Parameters:**
- `query` (string, Required): Natural language search query
- `category` (string, Optional): Filter by category
- `limit` (integer, Optional): Maximum results to return (default: 10)
- `since` (string, Optional): Time filter (e.g., '7 days ago', 'last week')

**Behavioral Requirements:**
- **Proactive Suggestions**: Surface relevant patterns automatically
- **Context Relevance**: Prioritize results by current context
- **Progressive Disclosure**: Essential results first, details on request

##### `insights`
**Description:** Get AI-powered insights from memory patterns

**Usage:** `/project:memory insights [args]`

**Aliases:** analyze, intelligence

**Parameters:**
- `focus` (string, Optional): Focus area for insights (values: performance, quality, workflow, team, architecture, all)
- `depth` (string, Optional):  (default: standard) (values: quick, standard, deep)
- `actionable` (boolean, Optional): Only show actionable insights

**Behavioral Requirements:**
- **Pattern Recognition**: Identify trends and successful approaches
- **Actionable Recommendations**: Provide specific next steps
- **Evidence Based**: Back insights with memory data

##### `patterns`
**Description:** Show recognized patterns in working style and project approach

**Usage:** `/project:memory patterns [args]`

**Aliases:** workflow-patterns, success-patterns, behavioral-patterns

**Parameters:**
- `type` (string, Optional): Pattern type to show (default: all) (values: workflow, decision, collaboration, quality, learning, technical, all)
- `success_rate` (string, Optional): Filter by success rate (default: all) (values: low, medium, high, critical, all)
- `context` (string, Optional): Pattern context scope (default: all) (values: current, project, team, personal, all)
- `timeframe` (string, Optional): Time period for pattern analysis (default: recent) (values: recent, month, quarter, year, all)

**Behavioral Requirements:**
- **Memory Integration**: Surface patterns from memory system
- **Evidence Based**: Show patterns backed by actual data
- **Actionable Insights**: Identify how to leverage successful patterns
- **Anti Pattern Awareness**: Highlight patterns to avoid
- **Progressive Disclosure**: Start with most relevant patterns

##### `bootstrap-memory`
**Description:** Bootstrap memory from existing codebase (brownfield)

**Usage:** `/project:memory bootstrap-memory [args]`

**Aliases:** bootstrap, mem-bootstrap, init-memory

**Parameters:**
- `mode` (string, Optional): Bootstrap mode (default: auto) (values: auto, interactive, guided)
- `focus` (string, Optional): Focus area (values: architecture, decisions, patterns, issues, all)
- `depth` (string, Optional): Analysis depth (default: standard) (values: shallow, standard, deep)
- `incremental` (boolean, Optional): Bootstrap incrementally for large projects
- `progress` (boolean, Optional): Show progress indicators (default: True)

**Behavioral Requirements:**
- **Pattern Extraction**: Identify existing successful patterns
- **Decision Documentation**: Capture architectural choices
- **Anti Pattern Detection**: Flag problematic code patterns
- **Context Understanding**: Build comprehensive project knowledge
- **Progress Tracking**: Display visual progress during execution
- **Error Recovery**: Handle failures gracefully with fallback options


#### Behavioral Requirements for Memory Operations
- **Structured Storage**: Categorize and tag all memory entries for efficient retrieval
- **Context Enrichment**: Add sufficient context for future understanding
- **Pattern Recognition**: Identify and capture reusable patterns and insights
- **Evidence Linking**: Connect memories to decisions and outcomes
- **Proactive Intelligence**: Surface relevant insights to prevent problems before they occur

#### Usage Examples
```bash
# Store technical decision with context
/project:memory remember "PostgreSQL chosen for ACID compliance needs" --category=decisions

# Recall authentication patterns
/project:memory recall "authentication best practices"

# Get actionable insights on architecture
/project:memory insights --focus=architecture --actionable

# Show recognized patterns in working style
/project:memory patterns --type=workflow --success-rate=high
```

---


### Quality Enforcement

**Claude Command:** `/project:quality [operation] [args]`

Enforce zero-tolerance quality standards through systematic validation, deep analysis, and anti-pattern prevention. Maintains excellence through behavioral compliance.

#### Available Operations

##### `udtm`
**Description:** Execute Ultra-Deep Thinking Mode for critical decisions

**Usage:** `/project:quality udtm [args]`

**Aliases:** ultra-deep, deep-think, udtm-analysis

**Parameters:**
- `topic` (string, Optional): Topic for analysis (interactive if not provided)
- `perspectives` (integer, Optional): Number of perspectives to analyze (default: 7)
- `depth` (string, Optional):  (default: standard) (values: quick, standard, deep, maximum)
- `evidence` (boolean, Optional): Require evidence for all claims (default: True)

**Behavioral Requirements:**
- **Structured Thinking**: Mandatory use of decision_analysis tags
- **Evidence Required**: All claims backed by verifiable data
- **Multiple Perspectives**: Consider minimum 3 viewpoints
- **Confidence Scoring**: Rate confidence in final recommendation

##### `quality-gate`
**Description:** Execute quality gate validation at project milestones

**Usage:** `/project:quality quality-gate [args]`

**Aliases:** qg, gate, checkpoint, validate

**Parameters:**
- `phase` (string, Required): Quality gate phase (values: pre-implementation, 25%, 50%, 75%, completion, custom)
- `strict` (boolean, Optional): Enforce strict validation (default: True)
- `report` (boolean, Optional): Generate detailed report (default: True)
- `fix` (boolean, Optional): Attempt automatic fixes

**Behavioral Requirements:**
- **Zero Tolerance**: No exceptions for critical quality standards
- **Evidence Based**: All quality assessments backed by data
- **Progressive Standards**: Higher requirements at later gates
- **Automated Fixes**: Attempt corrections before failing gate

##### `anti-pattern-check`
**Description:** Scan for prohibited patterns and architectural violations

**Usage:** `/project:quality anti-pattern-check [args]`

**Aliases:** anti-pattern, pattern-check, scan-violations

**Parameters:**
- `scope` (string, Optional): Scan scope (default: all) (values: current, changed, all, custom)
- `severity` (string, Optional): Minimum severity to report (default: all) (values: critical, high, medium, low, all)
- `autofix` (boolean, Optional): Attempt automatic fixes

**Behavioral Requirements:**
- **Zero False Positives**: Only flag actual violations
- **Graduated Penalties**: Penalties proportional to severity
- **Prevention First**: Warn before violation when possible
- **Learning Enabled**: Update patterns based on outcomes

##### `brotherhood-review`
**Description:** Initiate honest peer review process

**Usage:** `/project:quality brotherhood-review [args]`

**Aliases:** peer-review, brotherhood, review

**Parameters:**
- `reviewers` (integer, Optional): Number of reviewers (default: 2)
- `focus` (string, Optional): Review focus area (values: general, security, performance, architecture, quality)
- `anonymous` (boolean, Optional): Anonymous feedback

**Behavioral Requirements:**
- **Honest Feedback**: Direct, constructive criticism required
- **Evidence Based**: All feedback backed by specific examples
- **Improvement Focused**: Suggest specific enhancements
- **Brotherhood Spirit**: Supportive but uncompromising


#### Behavioral Requirements for Quality Enforcement
- **Zero Tolerance**: Binary accept/reject decisions with no exceptions
- **Evidence Required**: All quality assessments backed by specific data and metrics
- **Structured Analysis**: Mandatory use of quality_analysis tags
- **Penalty Enforcement**: 2x penalty multiplier for quality violations

#### Usage Examples
```bash
# Deep analysis for critical architectural decision
/project:quality udtm "microservices vs monolith for user management" --perspectives=7

# Run comprehensive quality gate validation
/project:quality quality-gate pre-implementation --strict --report

# Scan for anti-patterns across codebase
/project:quality anti-pattern-check --scope=all --autofix
```

---


### Workflow Management

**Claude Command:** `/project:workflow [operation] [args]`

Automate and manage development workflows with intelligent suggestions, structured handoffs, and comprehensive state management.

#### Available Operations

##### `suggest`
**Description:** Get AI-powered next step recommendations

**Usage:** `/project:workflow suggest [args]`

**Aliases:** next, recommend, what-next, advice

**Parameters:**
- `context` (string, Optional): Additional context for suggestions
- `confidence` (string, Optional): Minimum confidence level (default: medium) (values: low, medium, high, any)
- `alternatives` (integer, Optional): Number of alternatives (default: 1)

**Behavioral Requirements:**
- **Context Aware**: Consider current project state and goals
- **Confidence Scored**: Rate confidence in each suggestion
- **Actionable Steps**: Provide specific, implementable actions
- **Memory Enhanced**: Leverage past successful patterns

##### `handoff`
**Description:** Structured handoff between personas with context preservation

**Usage:** `/project:workflow handoff [args]`

**Aliases:** transfer, switch-to, pass-to

**Parameters:**
- `persona` (string, Required): Target persona (values: analyst, pm, architect, dev, sm, po, quality_enforcer, design-architect)
- `summary` (boolean, Optional): Include work summary (default: True)
- `checklist` (boolean, Optional): Run handoff checklist (default: True)
- `validate` (boolean, Optional): Validate handoff completeness (default: True)

**Behavioral Requirements:**
- **Context Preservation**: No information loss during handoff
- **Quality Continuity**: Maintain standards across personas
- **Structured Transition**: Use checklist for completeness
- **Memory Integration**: Document handoff insights

##### `core-dump`
**Description:** Save comprehensive session state with memory integration

**Usage:** `/project:workflow core-dump [args]`

**Aliases:** save-state, checkpoint, dump

**Parameters:**
- `format` (string, Optional): Dump format (default: standard) (values: minimal, standard, detailed, full)
- `include_memory` (boolean, Optional): Include memory insights (default: True)
- `compress` (boolean, Optional): Compress output

**Behavioral Requirements:**
- **Comprehensive Capture**: Include all relevant session state
- **Memory Integration**: Preserve learning and insights
- **Structured Format**: Organize for easy restoration
- **Progressive Disclosure**: Essential info first, details available

##### `tasks`
**Description:** List available tasks with intelligence insights

**Usage:** `/project:workflow tasks [args]`

**Aliases:** list-tasks, available-tasks, what-can-i-do

**Parameters:**
- `category` (string, Optional): Task category filter (values: all, quality, workflow, analysis, documentation)
- `recommended` (boolean, Optional): Show recommended tasks
- `details` (boolean, Optional): Show task details

**Behavioral Requirements:**
- **Context Aware**: Recommend tasks based on current state
- **Priority Ranking**: Order tasks by importance
- **Capability Matching**: Match tasks to current persona

##### `run-task`
**Description:** Execute a specific task

**Usage:** `/project:workflow run-task [args]`

**Aliases:** task, execute, do

**Parameters:**
- `task_name` (string, Required): Task to execute
- `args` (array, Optional): Task-specific arguments

**Behavioral Requirements:**
- **Task Validation**: Verify task exists and is appropriate
- **Parameter Validation**: Check required arguments
- **Quality Integration**: Apply quality standards during execution
- **Memory Enhancement**: Leverage relevant memories


#### Behavioral Requirements for Workflow Management
- **Context Preservation**: No information loss during workflow transitions
- **Quality Continuity**: Maintain standards across all workflow steps
- **Memory Integration**: Update and leverage system memory throughout workflow
- **Progressive Execution**: Break complex workflows into manageable, validated steps

#### Usage Examples
```bash
# Get intelligent next step suggestions
/project:workflow suggest --alternatives=3 --confidence=high

# Structured handoff from analyst to architect
/project:workflow handoff architect --summary --checklist

# Execute specific BMAD task
/project:workflow run-task create-prd
```

---


### Multi-Persona Consultation

**Claude Command:** `/project:consultation [operation] [args]`

Facilitate multi-persona collaboration for complex decisions requiring diverse perspectives and expertise synthesis.

#### Available Operations

##### `consult`
**Description:** Start multi-persona consultation session

**Usage:** `/project:consultation consult [args]`

**Aliases:** panel, team-consult, multi-persona

**Parameters:**
- `type` (string, Required): Consultation type (values: design-review, technical-feasibility, product-strategy, quality-assessment, emergency-response, custom)
- `personas` (array, Optional): Custom persona list (for custom type)
- `duration` (string, Optional): Consultation duration (default: standard) (values: quick, standard, thorough)
- `structured` (boolean, Optional): Use structured format (default: True)

**Behavioral Requirements:**
- **Diverse Perspectives**: Ensure all relevant viewpoints represented
- **Structured Process**: Follow consultation protocol
- **Consensus Building**: Work toward unified recommendations
- **Conflict Resolution**: Handle disagreements constructively

##### `panel-status`
**Description:** Show active consultation panel status

**Usage:** `/project:consultation panel-status [args]`

**Aliases:** consultation-status, panel-info

**Parameters:**
- `detailed` (boolean, Optional): Show detailed status
- `timeline` (boolean, Optional): Show consultation timeline

**Behavioral Requirements:**
- **Real Time Status**: Current state of consultation
- **Progress Tracking**: Show completion percentage
- **Participant Engagement**: Track individual contributions

##### `consensus-check`
**Description:** Assess agreement level in consultation

**Usage:** `/project:consultation consensus-check [args]`

**Aliases:** agreement, consensus, alignment

**Parameters:**
- `threshold` (integer, Optional): Consensus threshold percentage (default: 70)
- `require_all` (boolean, Optional): Require unanimous agreement

**Behavioral Requirements:**
- **Quantified Agreement**: Measure consensus percentage
- **Conflict Identification**: Highlight disagreement areas
- **Resolution Suggestions**: Recommend consensus-building approaches


#### Behavioral Requirements for Multi-Persona Consultation
- **Independent Analysis**: Each participant analyzes independently before collaboration
- **Evidence-Based Arguments**: All positions backed by verifiable data
- **Structured Synthesis**: Systematic integration of diverse perspectives
- **Consensus Documentation**: Clear recording of agreements and dissents

#### Usage Examples
```bash
# Start design review consultation
/project:consultation consult design-review --personas=architect,designer,quality

# Check consensus on technical decision
/project:consultation consensus-check --threshold=80

# View active consultation status
/project:consultation panel-status --detailed
```

---


### System Analysis

**Claude Command:** `/project:analysis [operation] [args]`

Perform comprehensive system analysis including diagnostics, optimization, and continuous learning from outcomes.

#### Available Operations

##### `diagnose`
**Description:** Comprehensive system health diagnostics

**Usage:** `/project:analysis diagnose [args]`

**Aliases:** health, check-system, diagnostic

**Parameters:**
- `component` (string, Optional): Component to diagnose (default: all) (values: all, memory, personas, tasks, quality, performance)
- `deep` (boolean, Optional): Perform deep diagnostics
- `fix` (boolean, Optional): Attempt automatic fixes

**Behavioral Requirements:**
- **Comprehensive Analysis**: Check all system components
- **Actionable Recommendations**: Provide specific fix suggestions
- **Priority Classification**: Rank issues by importance
- **Automated Fixes**: Attempt safe corrections when possible

##### `optimize`
**Description:** Performance optimization with memory-based improvements

**Usage:** `/project:analysis optimize [args]`

**Aliases:** perf, performance, tune

**Parameters:**
- `target` (string, Optional): Optimization target (default: balanced) (values: speed, memory, balanced, quality)
- `aggressive` (boolean, Optional): Use aggressive optimization
- `simulate` (boolean, Optional): Simulate without applying

**Behavioral Requirements:**
- **Memory Guided**: Use historical data for optimization decisions
- **Safe Improvements**: Avoid performance regressions
- **Measurable Gains**: Quantify optimization benefits
- **Rollback Capability**: Enable undo of optimizations

##### `learn`
**Description:** Analyze outcomes and update system intelligence

**Usage:** `/project:analysis learn [args]`

**Aliases:** ml-update, train, improve

**Parameters:**
- `scope` (string, Optional): Learning scope (default: session) (values: session, project, all)
- `feedback` (boolean, Optional): Include user feedback (default: True)
- `apply` (boolean, Optional): Apply learnings immediately (default: True)

**Behavioral Requirements:**
- **Pattern Extraction**: Identify successful approaches
- **Outcome Correlation**: Link actions to results
- **Continuous Improvement**: Update system behavior based on learning
- **Evidence Based**: Only apply well-supported learnings


#### Behavioral Requirements for System Analysis
- **Comprehensive Coverage**: Analyze all relevant system components and factors
- **Evidence-Based Conclusions**: All findings backed by measurable data
- **Actionable Recommendations**: Provide specific, implementable next steps
- **Memory Integration**: Update system intelligence based on analysis outcomes

#### Usage Examples
```bash
# Comprehensive system diagnostic
/project:analysis diagnose --component=performance --deep --fix

# Optimize for memory efficiency
/project:analysis optimize --target=memory --aggressive

# Learn from recent development outcomes
/project:analysis learn --scope=project --feedback
```

---


### Behavioral Tracking

**Claude Command:** `/project:behavioral [operation] [args]`

Track behavioral performance through gamification, achievements, and analytics. Motivate consistent excellence through scoring systems, streaks, and team rankings while maintaining privacy and user control.

#### Available Operations

##### `balance`
**Description:** Check current behavioral balance and status

**Usage:** `/project:behavioral balance [args]`

**Aliases:** bal, score, status-balance

**Parameters:**
- `detailed` (boolean, Optional): Show detailed recent activity
- `history` (boolean, Optional): Show full transaction history
- `trend` (boolean, Optional): Show balance trend analysis

**Behavioral Requirements:**
- **Real Time Tracking**: Current balance reflects all recent actions
- **Motivation Display**: Show progress toward next level/achievement
- **Transparent Calculation**: Clear breakdown of rewards and penalties
- **Actionable Insights**: Suggest specific improvement actions

##### `achievements`
**Description:** View unlocked achievements and progress toward new ones

**Usage:** `/project:behavioral achievements [args]`

**Aliases:** ach, awards, badges, accomplishments

**Parameters:**
- `category` (string, Optional): Achievement category filter (values: quality, speed, collaboration, innovation, learning, all)
- `available` (boolean, Optional): Show only unlocked achievements
- `progress` (boolean, Optional): Show in-progress achievements
- `stats` (boolean, Optional): Show achievement statistics

**Behavioral Requirements:**
- **Motivation Enhancement**: Celebrate completed achievements prominently
- **Progress Visibility**: Clear progress indicators for active achievements
- **Goal Clarity**: Specific criteria for earning each achievement
- **Social Recognition**: Team-appropriate achievement sharing

##### `streaks`
**Description:** Display active quality and efficiency streaks

**Usage:** `/project:behavioral streaks [args]`

**Aliases:** str, consistency, momentum

**Parameters:**
- `all` (boolean, Optional): Include broken and completed streaks
- `category` (string, Optional): Streak category filter (values: quality, efficiency, learning, collaboration, all)
- `potential` (boolean, Optional): Show potential streak opportunities

**Behavioral Requirements:**
- **Momentum Preservation**: Clear indication of streak requirements
- **Risk Awareness**: Warn about actions that could break streaks
- **Reward Anticipation**: Show upcoming streak milestone rewards
- **Recovery Guidance**: Help restart broken streaks

##### `leaderboard`
**Description:** View anonymized team rankings and performance

**Usage:** `/project:behavioral leaderboard [args]`

**Aliases:** lead, rankings, team-stats

**Parameters:**
- `timeframe` (string, Optional): Ranking timeframe (default: weekly) (values: daily, weekly, monthly, quarterly, all-time)
- `category` (string, Optional): Ranking category (default: overall) (values: overall, quality, speed, collaboration, innovation)
- `team` (string, Optional): Filter to specific team
- `anonymous` (boolean, Optional): Show anonymous rankings (default: True)

**Behavioral Requirements:**
- **Privacy Respect**: Maintain anonymity unless explicitly opted in
- **Healthy Competition**: Focus on improvement, not just ranking
- **Learning Opportunities**: Highlight successful approaches from top performers
- **Inclusive Recognition**: Multiple categories for different strengths

##### `behavioral-report`
**Description:** Generate detailed behavioral analytics and insights

**Usage:** `/project:behavioral behavioral-report [args]`

**Aliases:** behav, analytics, behavior-analysis, performance-report

**Parameters:**
- `period` (string, Optional): Analysis period (default: week) (values: day, week, month, quarter, year, custom)
- `focus` (string, Optional): Report focus area (default: comprehensive) (values: violations, rewards, patterns, improvement, trends, comprehensive)
- `compare` (string, Optional): Comparison baseline (values: team, previous-period, goals, industry)
- `export` (boolean, Optional): Export detailed data

**Behavioral Requirements:**
- **Actionable Insights**: Specific recommendations for improvement
- **Pattern Identification**: Recognition of behavioral trends
- **Goal Alignment**: Progress toward behavioral objectives
- **Predictive Guidance**: Proactive suggestions for success

##### `behavioral-preferences`
**Description:** Configure behavioral tracking and notification preferences

**Usage:** `/project:behavioral behavioral-preferences [args]`

**Aliases:** behav-prefs, behavior-settings, tracking-config

**Parameters:**
- `set` (string, Optional): Set preference key=value
- `get` (string, Optional): Get specific preference value
- `reset` (boolean, Optional): Reset all preferences to defaults

**Behavioral Requirements:**
- **User Control**: Full control over tracking and notifications
- **Privacy Options**: Granular privacy settings
- **Personalization**: Adapt to individual work styles
- **Reversible Changes**: Easy to modify or reset preferences


#### Behavioral Requirements for Behavioral Tracking
- **Real-Time Tracking**: Current balance reflects all recent actions and decisions
- **Motivation Enhancement**: Celebrate achievements and progress milestones prominently
- **Pattern Recognition**: Identify successful approaches and anti-patterns for improvement
- **Goal Alignment**: Track progress toward behavioral objectives and quality standards
- **Privacy Protection**: Maintain anonymity and user control over all tracking features
- **Gamification Balance**: Focus on improvement and learning, not just competition

#### Usage Examples
```bash
# Check current behavioral balance and trends
/project:behavioral balance --detailed --trend

# View achievements and progress
/project:behavioral achievements --category=quality --progress

# Show active quality streaks
/project:behavioral streaks --category=quality --potential

# View team performance rankings (anonymized)
/project:behavioral leaderboard --timeframe=weekly --anonymous

# Generate comprehensive behavioral analytics
/project:behavioral behavioral-report --period=monthly --focus=patterns

# Configure tracking preferences
/project:behavioral behavioral-preferences --set notifications=minimal
```

---


### System Management

**Claude Command:** `/project:system [operation] [args]`

Manage BMAD orchestrator initialization, configuration, health monitoring, and system validation. Provides essential infrastructure management and operational control for optimal system performance.

#### Available Operations

##### `init`
**Description:** Initialize BMAD orchestrator with configuration and memory

**Usage:** `/project:system init [args]`

**Aliases:** initialize, startup, boot, setup

**Parameters:**
- `config` (boolean, Optional): Load and validate configuration files (default: True)
- `memory` (boolean, Optional): Initialize memory system integration (default: True)
- `force` (boolean, Optional): Force re-initialization even if already initialized
- `minimal` (boolean, Optional): Minimal initialization for basic functionality

**Behavioral Requirements:**
- **Configuration Validation**: Verify all configuration files are valid
- **Memory Integration**: Establish connection to memory systems
- **Persona Validation**: Ensure all persona files are accessible
- **Quality Framework**: Initialize behavioral enforcement system
- **Session Preparation**: Prepare session state management

##### `status`
**Description:** Show BMAD orchestrator system status and health

**Usage:** `/project:system status [args]`

**Aliases:** health, system-status, info

**Parameters:**
- `detailed` (boolean, Optional): Show detailed status information
- `components` (boolean, Optional): Show individual component status
- `performance` (boolean, Optional): Include performance metrics

**Behavioral Requirements:**
- **Real Time Status**: Current operational state of all components
- **Health Indicators**: Clear indicators of system health
- **Performance Metrics**: Key performance indicators and trends
- **Issue Identification**: Highlight any problems or warnings

##### `config`
**Description:** Manage BMAD orchestrator configuration

**Usage:** `/project:system config [args]`

**Aliases:** configuration, settings, cfg

**Parameters:**
- `validate` (boolean, Optional): Validate configuration files
- `reload` (boolean, Optional): Reload configuration from files
- `backup` (boolean, Optional): Create configuration backup
- `restore` (string, Optional): Restore from backup file

**Behavioral Requirements:**
- **Configuration Integrity**: Ensure configuration files are valid and complete
- **Change Management**: Track and manage configuration changes
- **Backup Safety**: Reliable backup and restore capabilities
- **Validation Feedback**: Clear reporting of configuration issues

##### `session`
**Description:** Manage BMAD session state and persistence

**Usage:** `/project:system session [args]`

**Aliases:** session-state, state, persistence

**Parameters:**
- `save` (boolean, Optional): Save current session state
- `restore` (string, Optional): Restore from specific backup
- `new` (boolean, Optional): Start new session
- `info` (boolean, Optional): Show session information (default: True)

**Behavioral Requirements:**
- **State Preservation**: Reliable preservation of session context and progress
- **Seamless Restoration**: Smooth restoration of previous session state
- **Session Continuity**: Maintain context across session boundaries
- **Data Integrity**: Ensure session data remains consistent and valid

##### `validate`
**Description:** Comprehensive system validation and health check

**Usage:** `/project:system validate [args]`

**Aliases:** verify, check, validation, health-check

**Parameters:**
- `full` (boolean, Optional): Perform comprehensive validation
- `memory` (boolean, Optional): Focus on memory system validation
- `personas` (boolean, Optional): Focus on persona system validation
- `fix` (boolean, Optional): Attempt automatic fixes for issues
- `report` (boolean, Optional): Generate detailed validation report (default: True)

**Behavioral Requirements:**
- **Comprehensive Checking**: Validate all critical system components
- **Issue Identification**: Clearly identify problems and their severity
- **Automated Recovery**: Attempt safe automatic fixes where possible
- **Detailed Reporting**: Provide actionable validation reports


#### Behavioral Requirements for System Management
- **Configuration Integrity**: Ensure all configuration files are valid and complete
- **Change Management**: Track and safely manage configuration changes with rollback
- **Health Monitoring**: Real-time status tracking with proactive issue identification
- **Session Persistence**: Reliable state management across session boundaries
- **Automated Recovery**: Attempt safe fixes for common problems before escalation
- **Operational Excellence**: Monitor and optimize system performance continuously

#### Usage Examples
```bash
# Initialize BMAD orchestrator with full setup
/project:system init --config --memory

# Check comprehensive system health
/project:system status --detailed --components --performance

# Validate configuration files
/project:system config --validate --backup

# Save current session state
/project:system session --save

# Run comprehensive system validation
/project:system validate --full --fix --report
```

---


### Core Operations

**Claude Command:** `/project:core [operation] [args]`

Essential operations providing contextual assistance, persona information, system guidance, and orchestrator functions including help, context display, and session management.

#### Available Operations

##### `help`
**Description:** Display contextual help with memory-enhanced suggestions

**Usage:** `/project:core help [args]`

**Aliases:** h, ?, help-me, assist

**Parameters:**
- `topic` (string, Optional): Specific help topic (values: commands, personas, workflow, memory, quality, consultation)
- `examples` (boolean, Optional): Show usage examples
- `advanced` (boolean, Optional): Show advanced options

**Behavioral Requirements:**
- **Example Reference**: Include relevant examples from help topics
- **Progressive Disclosure**: Start with essential info, expand on request
- **Context Awareness**: Adapt help based on user expertise level

##### `agents`
**Description:** List available personas with usage statistics and insights

**Usage:** `/project:core agents [args]`

**Aliases:** personas, list, who, team

**Parameters:**
- `stats` (boolean, Optional): Include usage statistics
- `recommended` (boolean, Optional): Show AI-recommended personas for current context
- `details` (boolean, Optional): Show detailed persona descriptions

**Behavioral Requirements:**
- **Context Awareness**: Recommend personas based on current project context
- **Progressive Disclosure**: Show essential persona info first
- **Example Usage**: Include examples of when to use each persona

##### `context`
**Description:** Display and manage project context without technical identifiers

**Usage:** `/project:core context [args]`

**Aliases:** ctx, status, where, state, info

**Parameters:**
- `action` (string, Optional):  (values: save, restore, search)
- `name` (string, Optional): Context checkpoint name
- `query` (string, Optional): Search query for context
- `full` (boolean, Optional): Show full context details

**Behavioral Requirements:**
- **Memory Integration**: Surface relevant memories for current context
- **Proactive Suggestions**: Recommend next steps based on context
- **Progressive Disclosure**: Essential context first, details on request
- **No Technical Ids**: Never expose session IDs or technical identifiers

##### `checklist`
**Description:** Run validation checklist

**Usage:** `/project:core checklist [args]`

**Aliases:** check, validate, run-checklist

**Parameters:**
- `name` (string, Required): Checklist name (values: po-master, story-dod, architect, quality, frontend, pm, change)
- `interactive` (boolean, Optional): Interactive mode
- `fix` (boolean, Optional): Attempt fixes

**Behavioral Requirements:**
- **Comprehensive Validation**: Check all checklist items
- **Evidence Collection**: Gather proof for each requirement
- **Automated Fixes**: Attempt corrections where possible
- **Clear Reporting**: Provide actionable feedback

##### `exit`
**Description:** Exit current persona or consultation

**Usage:** `/project:core exit [args]`

**Aliases:** quit, leave, close

**Parameters:**
- `save` (boolean, Optional): Save current state (default: True)
- `handoff` (boolean, Optional): Suggest handoff target

**Behavioral Requirements:**
- **State Preservation**: Save progress and insights
- **Clean Transitions**: Proper context closure
- **Handoff Suggestions**: Recommend appropriate next persona

##### `yolo`
**Description:** Toggle YOLO mode for streamlined execution

**Usage:** `/project:core yolo [args]`

**Aliases:** fast-mode, quick, bypass

**Parameters:**
- `confirm` (boolean, Optional): Confirm mode change

**Behavioral Requirements:**
- **Safety Maintenance**: Never compromise critical safety rules
- **Speed Optimization**: Reduce process overhead
- **Quality Awareness**: Maintain minimum quality standards
- **User Consent**: Require explicit confirmation


#### Behavioral Requirements for Core Operations
- **Progressive Disclosure**: Provide essential information first, details on request
- **Context Awareness**: Adapt responses to user expertise and project phase
- **Memory Enhanced**: Surface relevant memories and successful patterns
- **Example Driven**: Include relevant examples from BMAD library
- **State Management**: Proper preservation of context across operations
- **Orchestrator Functions**: Support session management and persona coordination

#### Usage Examples
```bash
# Get help on persona system
/project:core help personas --examples

# List available personas with recommendations
/project:core agents --stats --recommended

# Show rich context with suggestions
/project:core context --full --memory --suggestions

# Exit current persona with state preservation
/project:core exit --save --handoff

# Toggle YOLO mode for streamlined execution
/project:core yolo --confirm
```

---


## Integration Notes

### Claude Code Specific Features
- **Command Completion**: Type `/project:` to see available command groups
- **Argument Handling**: All text after the command becomes `$ARGUMENTS`
- **Project Context**: Commands automatically access your project context
- **Session Persistence**: Memory operations persist across Claude Code sessions

### BMAD Method Integration
- **Persona Continuity**: Activated personas maintain state throughout session
- **Quality Gates**: Automatic quality validation at key checkpoints
- **Memory Enhancement**: All interactions contribute to system learning
- **Behavioral Tracking**: Anti-pattern detection and behavioral optimization

### Team Collaboration
- **Shared Commands**: All team members can use the same command set
- **Consistent Behavior**: BMAD framework ensures consistent AI behavior
- **Knowledge Sharing**: Memory operations capture and share team insights
- **Quality Standards**: Unified quality enforcement across team

## Troubleshooting

### Command Not Found
- Ensure `.claude/commands/` directory exists in project root
- Verify command files are present: `ls .claude/commands/`
- Check file permissions and syntax

### Behavioral Framework Issues
- Commands automatically enforce BMAD behavioral requirements
- Anti-patterns trigger immediate penalties and corrections
- Quality gates may block progress until standards are met
- Use `/project:core help` for behavioral guidance

### Memory System Issues  
- Memory operations require proper categorization and tagging
- Bootstrap memory from existing codebases with `/project:memory bootstrap-memory`
- Use `/project:memory insights` to verify memory system health

## Advanced Usage

### Workflow Patterns
```bash
# Analysis → Design → Implementation workflow
/project:persona analyst
/project:analysis diagnose --component=architecture
/project:workflow handoff architect
/project:persona architect
/project:quality quality-gate pre-implementation
```

### Quality-First Development
```bash
# Deep thinking for critical decisions
/project:quality udtm "authentication system design" --perspectives=7
/project:quality anti-pattern-check --scope=all
/project:quality brotherhood-review --focus=security
```

### Memory-Enhanced Learning
```bash
# Capture and leverage organizational knowledge
/project:memory remember "JWT tokens expire in 1 hour for security" --category=decisions
/project:memory recall "authentication best practices"
/project:memory insights --focus=security --actionable
```

### Multi-Persona Consultation
```bash
# Complex decision making with multiple perspectives
/project:consultation consult design-review --personas=architect,designer,quality
/project:consultation consensus-check --threshold=80
```

---

**Generated by BMAD Method Documentation System**  
**Last Updated:** 2025-06-06 01:45:28 UTC  
**Source:** bmad-agent/commands/command-registry.yml  
**Command Count:** 49 total commands across 9 groups
