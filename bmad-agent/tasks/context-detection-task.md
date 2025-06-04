# Context Detection Task

## Purpose
Automatically detect project context, team experience level, current phase, and technical stack to enable intelligent instruction adaptation. This task runs at session start and periodically during execution.

## Detection Protocol

### Phase 1: Initial Scan (Automatic at Start)
1. **Project Type Detection**
   ```bash
   # Check for new vs existing project
   if [ ! -d ".git" ] || [ $(git rev-list --count HEAD 2>/dev/null || echo 0) -lt 5 ]; then
     PROJECT_TYPE="greenfield"
   else
     PROJECT_TYPE="brownfield"
   fi
   
   # Check for MVP indicators
   if grep -i "mvp\|prototype\|poc" README.md 2>/dev/null; then
     PROJECT_VARIANT="mvp"
   fi
   ```

2. **Codebase Analysis**
   - File count and structure
   - Primary languages detection
   - Framework identification
   - Dependency analysis

3. **Team Experience Indicators**
   - Question complexity analysis
   - Error frequency patterns
   - Tool usage proficiency
   - BMAD method familiarity

4. **Current Phase Detection**
   - Commit message patterns
   - File modification patterns
   - Task/story status
   - Branch naming conventions

### Phase 2: Context Synthesis
Combine all indicators to determine:
- Primary context type
- Experience level
- Current phase
- Applicable adaptations

### Phase 3: Adaptation Application
1. Load appropriate instruction set
2. Configure verbosity level
3. Set safety thresholds
4. Select relevant examples

## Detection Rules

### Project Type Indicators
```yaml
greenfield_indicators:
  strong:
    - No .git directory
    - <100 files in project
    - No package.json/requirements.txt
    - Empty or minimal README
  moderate:
    - <5 commits in repository
    - Single contributor
    - No CI/CD configuration
    - Basic project structure

brownfield_indicators:
  strong:
    - >10K lines of code
    - >50 commits
    - Multiple contributors
    - Established folder structure
  moderate:
    - Legacy dependencies
    - TODO/FIXME comments
    - Deprecation warnings
    - Technical debt markers

mvp_indicators:
  strong:
    - "MVP" in project name
    - Timeline <3 months
    - Minimal feature set
    - "Validate" in objectives
  moderate:
    - Prototype branches
    - Experimental flags
    - Quick iteration pattern
    - Limited test coverage
```

### Experience Level Detection
```yaml
experience_signals:
  junior:
    questions:
      - "What is...?"
      - "How do I...?"
      - "Can you explain...?"
      - Basic syntax queries
    errors:
      - Syntax errors frequent
      - Conceptual confusion
      - Tool usage mistakes
    patterns:
      - Step-by-step needs
      - Clarification requests
      - Example dependence
      
  intermediate:
    questions:
      - "Best way to...?"
      - "Should I use X or Y?"
      - Architecture queries
    errors:
      - Logic errors
      - Integration issues
      - Optimization needs
    patterns:
      - Some autonomy
      - Pattern recognition
      - Selective help
      
  senior:
    questions:
      - "Trade-offs between...?"
      - "Performance impact of...?"
      - Edge case handling
    errors:
      - Rare
      - Complex scenarios
      - System-level issues
    patterns:
      - High autonomy
      - Meta discussions
      - Teaching others
```

### Phase Detection Logic
```yaml
phase_detection:
  inception:
    markers:
      - No PRD exists
      - Research tasks active
      - Brainstorming mode
      - Requirements gathering
      
  planning:
    markers:
      - PRD in progress
      - Architecture design
      - Technology selection
      - Estimation occurring
      
  development:
    markers:
      - Active story implementation
      - Regular commits
      - Test writing
      - Code reviews
      
  stabilization:
    markers:
      - Bug fix commits
      - Performance tuning
      - Documentation updates
      - Release preparation
      
  maintenance:
    markers:
      - Production hotfixes
      - Dependency updates
      - Security patches
      - Technical debt work
```

## Output Format
```yaml
context_detection_result:
  project:
    type: "greenfield|brownfield|mvp|enterprise"
    confidence: 85
    evidence:
      - "No existing codebase"
      - "New repository created today"
      
  team:
    experience: "junior|intermediate|senior|expert"
    confidence: 90
    evidence:
      - "Basic questions asked"
      - "Frequent clarifications needed"
      
  phase:
    current: "inception|planning|development|stabilization|maintenance"
    confidence: 75
    evidence:
      - "No PRD found"
      - "Research tasks active"
      
  stack:
    category: "modern_web|traditional_web|api_first|microservices|serverless"
    technologies: ["React", "TypeScript", "Node.js"]
    confidence: 95
    
  recommended_adaptations:
    instruction_style: "educational"
    verbosity_level: "detailed"
    example_count: 5
    safety_level: "protective"
    validation_frequency: "every_step"
```

## Integration Points
- Runs automatically at session start
- Updates when significant changes detected
- Can be triggered manually via `/context detect`
- Results stored in memory for pattern learning
- Influences all subsequent interactions

## Override Mechanism
Users can override detection with:
- `/context set greenfield` - Force project type
- `/experience senior` - Set experience level
- `/phase development` - Specify current phase
- `/context auto` - Return to automatic detection

## Success Criteria
- 95% accurate context detection
- <500ms detection time
- Seamless adaptation application
- User satisfaction with adapted behavior