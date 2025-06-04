# Context-Aware Instruction System

## Core Principle
Instructions dynamically adapt based on project context, team experience, and current state. The system detects context automatically and modifies behavior to optimize for success in each unique situation.

## Context Detection Framework

### 1. Project Type Identification
```yaml
project_types:
  greenfield:
    indicators:
      - No existing codebase
      - New repository
      - Initial commit phase
      - No legacy constraints
    adaptations:
      - Emphasis on exploration
      - Flexible architecture choices
      - More time for research
      - Higher experimentation tolerance
      
  brownfield:
    indicators:
      - Existing codebase >10K LOC
      - Multiple contributors
      - Production deployment
      - Legacy dependencies
    adaptations:
      - Conservative approach
      - Compatibility focus
      - Incremental changes
      - Regression prevention
      
  mvp:
    indicators:
      - "MVP" in project name/description
      - Timeline <3 months
      - Limited feature scope
      - Validation focus
    adaptations:
      - Core features only
      - Defer optimization
      - Rapid iteration
      - Technical debt acceptance
      
  enterprise:
    indicators:
      - Compliance requirements
      - Multiple stakeholders
      - Audit trails required
      - High availability needs
    adaptations:
      - Full documentation
      - Extensive testing
      - Security first
      - Change control process
```

### 2. Team Experience Assessment
```yaml
experience_levels:
  junior:
    indicators:
      - First-time BMAD users
      - Limited domain knowledge
      - Frequent clarifications
      - Basic questions asked
    adaptations:
      - Extra examples provided
      - Step-by-step guidance
      - Simplified terminology
      - Proactive explanations
      
  intermediate:
    indicators:
      - 3-6 months BMAD usage
      - Domain familiarity
      - Occasional clarifications
      - Pattern recognition
    adaptations:
      - Standard instructions
      - Balanced guidance
      - Technical details included
      - Some autonomy assumed
      
  senior:
    indicators:
      - 6+ months BMAD usage
      - Deep domain expertise
      - Rare clarifications
      - Advanced questions
    adaptations:
      - Concise instructions
      - Advanced features enabled
      - Minimal hand-holding
      - Expert shortcuts available
      
  expert:
    indicators:
      - BMAD power user
      - Cross-domain expertise
      - No clarifications needed
      - Optimization focus
    adaptations:
      - Tersest instructions
      - Full feature access
      - Custom workflows
      - Meta-level operations
```

### 3. Project Phase Detection
```yaml
project_phases:
  inception:
    indicators:
      - No PRD exists
      - Requirements gathering
      - Stakeholder interviews
      - Market research active
    adaptations:
      - Discovery emphasis
      - Brainstorming encouraged
      - Flexible planning
      - Wide exploration
      
  planning:
    indicators:
      - PRD in progress
      - Architecture design
      - Technology selection
      - Team formation
    adaptations:
      - Decision support
      - Alternative analysis
      - Risk assessment focus
      - Evidence gathering
      
  development:
    indicators:
      - Active coding
      - Story implementation
      - Regular commits
      - Sprint execution
    adaptations:
      - Implementation focus
      - Quality gates enforced
      - Testing emphasis
      - Performance monitoring
      
  stabilization:
    indicators:
      - Feature complete
      - Bug fixing mode
      - Performance tuning
      - Release preparation
    adaptations:
      - Zero defect tolerance
      - Regression prevention
      - Documentation completion
      - Deployment readiness
      
  maintenance:
    indicators:
      - Production system
      - Bug reports incoming
      - Enhancement requests
      - Technical debt work
    adaptations:
      - Stability first
      - Careful changes
      - Comprehensive testing
      - Rollback planning
```

### 4. Technical Stack Recognition
```yaml
stack_categories:
  modern_web:
    indicators: [React, Vue, Next.js, TypeScript, Vite]
    adaptations:
      - Component-driven design
      - State management patterns
      - Build optimization focus
      - Type safety enforcement
      
  traditional_web:
    indicators: [jQuery, PHP, WordPress, Apache]
    adaptations:
      - Progressive enhancement
      - Server-side focus
      - Plugin architecture
      - Compatibility emphasis
      
  api_first:
    indicators: [REST, GraphQL, gRPC, OpenAPI]
    adaptations:
      - Contract-first design
      - Versioning strategies
      - Documentation priority
      - Client SDK generation
      
  microservices:
    indicators: [Docker, Kubernetes, Service Mesh]
    adaptations:
      - Distributed patterns
      - Service boundaries
      - Orchestration focus
      - Observability requirements
      
  serverless:
    indicators: [Lambda, Functions, Vercel, Netlify]
    adaptations:
      - Event-driven design
      - Cold start optimization
      - Stateless patterns
      - Cost optimization
```

## Instruction Adaptation Rules

### 1. Complexity Adjustment
```yaml
complexity_matrix:
  junior_greenfield:
    level: simplified
    features:
      - Basic patterns only
      - Extensive comments
      - Error prevention focus
      - Guided decisions
      
  junior_brownfield:
    level: cautious
    features:
      - Extra safety checks
      - Detailed impact analysis
      - Step-by-step changes
      - Rollback emphasis
      
  senior_greenfield:
    level: advanced
    features:
      - Complex patterns allowed
      - Minimal comments
      - Performance optimization
      - Autonomous decisions
      
  senior_brownfield:
    level: strategic
    features:
      - Refactoring enabled
      - Architecture evolution
      - Technical debt reduction
      - System modernization
```

### 2. Verbosity Control
```yaml
verbosity_rules:
  conditions:
    - if: team.experience == "junior" && project.phase == "inception"
      then: verbosity = "detailed"
      
    - if: team.experience == "expert" && project.phase == "development"
      then: verbosity = "minimal"
      
    - if: project.type == "mvp" && time.pressure == "high"
      then: verbosity = "essential"
      
    - if: project.type == "enterprise" && audit.required == true
      then: verbosity = "comprehensive"
      
  levels:
    minimal:
      max_lines: 4
      include: [answer, code]
      exclude: [explanation, examples]
      
    essential:
      max_lines: 10
      include: [answer, code, key_points]
      exclude: [detailed_explanation]
      
    standard:
      max_lines: 20
      include: [answer, code, explanation, example]
      exclude: [alternative_approaches]
      
    detailed:
      max_lines: 50
      include: [everything]
      exclude: []
```

### 3. Safety Threshold Adaptation
```yaml
safety_thresholds:
  junior_mvp:
    anti_patterns: strict
    testing: basic
    documentation: essential
    review: recommended
    
  junior_production:
    anti_patterns: zero_tolerance
    testing: comprehensive
    documentation: complete
    review: mandatory
    
  senior_mvp:
    anti_patterns: standard
    testing: critical_paths
    documentation: inline
    review: optional
    
  senior_production:
    anti_patterns: strict
    testing: comprehensive
    documentation: architectural
    review: peer_required
```

### 4. Example Selection
```yaml
example_selection:
  rules:
    - if: team.experience == "junior"
      then: 
        - show_bad_examples: true
        - example_count: 3-5
        - complexity: basic
        
    - if: project.type == "similar_to_previous"
      then:
        - use_historical_examples: true
        - show_success_patterns: true
        - reference_past_decisions: true
        
    - if: technical.stack == "unfamiliar"
      then:
        - provide_stack_examples: true
        - include_documentation_links: true
        - show_integration_patterns: true
```

## Dynamic Prompt Modification

### 1. Conditional Instruction Blocks
```markdown
<!-- IF project.type == "greenfield" -->
## Architecture Freedom
You have full freedom to choose the optimal architecture. Consider:
- Modern patterns and practices
- Team skillset alignment
- Future scalability needs
- No legacy constraints
<!-- ENDIF -->

<!-- IF project.type == "brownfield" -->
## Legacy Compatibility
You must maintain compatibility with existing systems:
- Preserve current interfaces
- Gradual migration approach
- Minimize breaking changes
- Test regression thoroughly
<!-- ENDIF -->

<!-- IF team.experience == "junior" -->
## Step-by-Step Guidance
Let's work through this together:
1. First, we'll understand the problem
2. Then explore simple solutions
3. We'll validate each step
4. Finally, implement with tests

Remember: It's okay to ask questions!
<!-- ENDIF -->
```

### 2. Context-Specific Examples
```yaml
example_injection:
  mvp_context:
    - "For MVP, we'll use SQLite instead of PostgreSQL"
    - "Skip caching layer until we validate product-market fit"
    - "Use managed services to reduce operational overhead"
    
  enterprise_context:
    - "Implement full audit logging from day one"
    - "Use enterprise-grade message queue (e.g., IBM MQ)"
    - "Include disaster recovery in initial design"
    
  junior_context:
    - "Here's a working example you can adapt"
    - "Common mistake to avoid: [specific anti-pattern]"
    - "If confused, this tutorial explains it well: [link]"
```

### 3. Adapted Safety Rules
```yaml
safety_adaptations:
  high_risk_context:
    rules:
      - "MANDATORY: Every change requires approval"
      - "REQUIRED: Full regression test suite"
      - "CRITICAL: Zero downtime deployment"
      
  low_risk_context:
    rules:
      - "RECOMMENDED: Peer review for major changes"
      - "SUGGESTED: Test critical paths"
      - "OPTIONAL: Canary deployment"
      
  learning_context:
    rules:
      - "ENCOURAGED: Experiment with approaches"
      - "ACCEPTABLE: Controlled technical debt"
      - "IMPORTANT: Document learnings"
```

## Learning and Optimization

### 1. Pattern Recognition
```yaml
pattern_tracking:
  success_patterns:
    - context: {type: "mvp", team: "junior", phase: "development"}
      pattern: "Pair programming sessions"
      success_rate: 85%
      
    - context: {type: "enterprise", team: "senior", phase: "planning"}
      pattern: "Formal architecture reviews"
      success_rate: 92%
      
  failure_patterns:
    - context: {type: "brownfield", team: "junior", phase: "refactoring"}
      pattern: "Big bang refactoring"
      failure_rate: 73%
      recommendation: "Incremental refactoring"
```

### 2. Team Preference Learning
```yaml
team_preferences:
  team_alpha:
    communication_style: concise
    documentation_preference: inline
    review_style: async
    tool_preferences: [VSCode, Git, Docker]
    
  team_beta:
    communication_style: detailed
    documentation_preference: comprehensive
    review_style: pair_programming
    tool_preferences: [IntelliJ, GitHub, Kubernetes]
```

### 3. Automatic Optimization
```yaml
optimization_rules:
  - trigger: "Same question asked 3+ times"
    action: "Add to FAQ, adjust default explanation"
    
  - trigger: "Consistent pattern success"
    action: "Promote to recommended approach"
    
  - trigger: "Repeated context misidentification"
    action: "Refine detection indicators"
    
  - trigger: "Instruction ignored repeatedly"
    action: "Simplify or emphasize differently"
```

## Context Override Mechanisms

### 1. Explicit Overrides
```yaml
override_commands:
  "/context set [type]": Force specific context type
  "/experience [level]": Override experience detection
  "/verbosity [level]": Set instruction detail level
  "/safety [level]": Adjust safety thresholds
  "/examples [on|off]": Toggle example inclusion
```

### 2. Temporary Adjustments
```yaml
temporary_modes:
  emergency:
    duration: "Until explicitly cleared"
    changes:
      - Skip non-critical validations
      - Direct implementation mode
      - Minimal documentation
      - Fast decision making
      
  learning:
    duration: "Current session"
    changes:
      - Extra explanations
      - More examples
      - Slower pace
      - Encouraging tone
      
  audit:
    duration: "Current task"
    changes:
      - Full documentation
      - Complete audit trail
      - All decisions logged
      - Evidence required
```

## Performance Tracking

### 1. Context Effectiveness Metrics
```yaml
metrics:
  detection_accuracy:
    target: 95%
    measurement: "Correct context identification"
    
  adaptation_success:
    target: 90%
    measurement: "Task completed without context issues"
    
  user_satisfaction:
    target: 4.5/5
    measurement: "Context-appropriate responses"
    
  instruction_efficiency:
    target: 80%
    measurement: "First-attempt understanding"
```

### 2. Continuous Improvement
```yaml
improvement_cycle:
  weekly:
    - Review context misidentifications
    - Update detection indicators
    - Refine adaptation rules
    
  monthly:
    - Analyze success patterns
    - Update team preferences
    - Optimize instruction sets
    
  quarterly:
    - Major pattern review
    - Context category updates
    - System effectiveness audit
```

## Integration Points

### With Memory System
- Store context detection results
- Learn team preferences over time
- Track successful adaptations
- Build pattern library

### With Personas
- Each persona adapts to context
- Shared context awareness
- Consistent adaptations
- Role-specific adjustments

### With Quality Gates
- Context-appropriate thresholds
- Phase-specific requirements
- Experience-based validation
- Risk-adjusted criteria

## Success Indicators

### Quantitative
- 95% context detection accuracy
- 90% appropriate adaptation rate
- 50% reduction in clarification requests
- 80% improved task completion speed

### Qualitative
- Natural feeling interactions
- Reduced user frustration
- Better team alignment
- Improved project outcomes

Remember: Context awareness isn't about guessing—it's about recognizing patterns and adapting intelligently to optimize for success in each unique situation.