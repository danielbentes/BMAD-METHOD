# Memory Bootstrap Task for Brownfield Projects

## Purpose
Rapidly establish comprehensive contextual memory for existing projects by systematically analyzing project artifacts, extracting decisions, identifying patterns, and creating foundational memory entries for immediate BMAD memory-enhanced operations. Generate bootstrap reports at `.bmad/history/bootstrap-reports/bootstrap-{timestamp}.md`.

## ⚡ CRITICAL EXECUTION REQUIREMENTS

**MANDATORY**: This task requires ACTUAL MEMORY CREATION, not just analysis.

### Execution Protocol
1. **Analyze** project artifacts (as detailed below)
2. **CREATE** memory entries using `add_memories()` function for each insight
3. **VERIFY** memory creation success after each call
4. **DOCUMENT** total memories created in final report
5. **VALIDATE** core purpose achieved: "Are memories now stored in the system?"

### Error Handling
- If `add_memories()` fails: Store entries in session state for later sync
- If memory system unavailable: Document entries in `.bmad/system/memory/fallbacks/bootstrap-memories.md` 
- Always attempt memory creation - don't assume unavailability without testing

### Success Criteria
- **MINIMUM**: 5 memories created across different categories
- **TARGET**: 10-15 memories for comprehensive bootstrap
- **VERIFICATION**: Can search and retrieve created memories

## Bootstrap Process Overview

### Phase 1: Project Context Discovery (10-15 minutes)
**Goal**: Understand current project state and establish baseline context

### Phase 2: Decision Archaeology (15-20 minutes)  
**Goal**: Extract and document key architectural and strategic decisions made in the project

### Phase 3: Pattern Mining (10-15 minutes)
**Goal**: Identify existing conventions, approaches, and successful patterns

### Phase 4: Issue/Solution Mapping (10-15 minutes)
**Goal**: Document known problems, their solutions, and technical debt

### Phase 5: Preference & Style Inference (5-10 minutes)
**Goal**: Understand team working style and project-specific preferences

## Progress Tracking

### Visual Progress Indicators
Display progress during bootstrap execution:
```
🔄 Memory Bootstrap Progress
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Phase 1: Project Discovery    [████████░░] 80%
Phase 2: Decision Analysis    [████░░░░░░] 40%
Phase 3: Pattern Mining       [░░░░░░░░░░] 0%
Phase 4: Issue Mapping        [░░░░░░░░░░] 0%
Phase 5: Style Inference      [░░░░░░░░░░] 0%
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
⏱️  Elapsed: 12 minutes | Est. Remaining: 18 minutes
📝 Memories Created: 7 | Target: 10-15
```

## Incremental Bootstrap Support

### Large Project Strategy
For projects with >1000 files or complex structures:

1. **Phased Analysis**
   ```
   Phase 1: Core modules only (src/core, lib/main)
   Phase 2: Feature modules (src/features/*)
   Phase 3: Tests and utilities
   Phase 4: Documentation and configs
   ```

2. **Checkpoint System**
   - Save progress after each major phase
   - Allow resumption from last checkpoint
   - Store partial results in `.bmad/bootstrap/checkpoints/`

3. **Memory Batching**
   - Create memories in batches of 5-10
   - Validate each batch before proceeding
   - Prevent memory system overload

## Enhanced Error Handling

### Error Recovery Protocol
```python
try:
    # Attempt memory creation
    add_memories(content, tags, metadata)
except MemorySystemError as e:
    # Fallback 1: Queue for retry
    queue_for_retry(content, tags, metadata)
    log_error(f"Memory creation failed: {e}")
except ConnectionError as e:
    # Fallback 2: Local storage
    save_to_fallback(content, tags, metadata)
    log_warning(f"Using fallback storage: {e}")
except Exception as e:
    # Fallback 3: Critical error handling
    save_critical_data(content)
    notify_user(f"Bootstrap error: {e}")
    provide_recovery_options()
```

### Validation Checkpoints
- After each phase: Verify memories were created
- Check memory retrieval works before proceeding
- Validate data integrity and relationships

## Execution Instructions

### Phase 1: Project Context Discovery

#### 1.1 Scan Project Structure
```bash
# Command to initiate bootstrap
/bootstrap-memory
```

**Analysis Steps:**
1. **Examine Repository Structure**: Analyze folder organization, naming conventions, separation of concerns
2. **Identify Technology Stack**: Extract from package.json, requirements.txt, dependencies, build files
3. **Documentation Review**: Scan README, docs/, wikis, inline documentation
4. **Architecture Discovery**: Look for architecture diagrams, technical documents, design decisions

**Memory Creation:**
```json
{
  "type": "project-context",
  "project_name": "extracted-or-asked",
  "project_type": "brownfield-analysis",
  "technology_stack": ["extracted-technologies"],
  "architecture_style": "inferred-from-structure",
  "repository_structure": "analyzed-organization-pattern",
  "documentation_maturity": "assessed-level",
  "team_size_inference": "based-on-commit-patterns",
  "project_age": "estimated-from-history",
  "active_development": "current-activity-level"
}
```

#### 1.2 Current State Assessment
**Questions to Ask User:**
1. "What's the current phase of this project? (Active development, maintenance, scaling, refactoring)"
2. "What are the main pain points or challenges you're facing?"
3. "What's working well that we should preserve?"
4. "Are there any major changes or decisions being considered?"

### Phase 2: Decision Archaeology

#### 2.1 Extract Technical Decisions
**Analysis Areas:**
- **Database Choices**: Why PostgreSQL vs MongoDB? What drove the decision?
- **Framework Selection**: Why React/Angular/Vue? What were the alternatives?
- **Architecture Patterns**: Microservices vs Monolith? Event-driven? RESTful APIs?
- **Deployment Strategy**: Cloud provider choice, containerization decisions
- **Testing Strategy**: Testing frameworks, coverage expectations, E2E approaches

**Memory Creation Template:**
```json
{
  "type": "decision",
  "project": "current-project",
  "persona": "inferred-from-context",
  "decision": "framework-choice-react",
  "rationale": "extracted-or-inferred-reasoning",
  "alternatives_considered": ["vue", "angular", "vanilla"],
  "constraints": ["team-expertise", "timeline", "ecosystem"],
  "outcome": "successful", // inferred from current usage
  "evidence": "still-in-use-and-maintained",
  "context_tags": ["frontend", "framework", "team-decision"],
  "confidence_level": "medium-inferred"
}
```

#### 2.2 Business/Product Decisions
**Extract:**
- **Feature Prioritization**: What features were built first and why?
- **User Experience Choices**: Key UX decisions and their rationale
- **Scope Decisions**: What was explicitly left out of MVP and why?
- **Market Positioning**: Target users, competitive positioning

### Phase 3: Pattern Mining

#### 3.1 Code Pattern Analysis
**Identify:**
- **Coding Conventions**: Naming, file organization, component structure
- **Architecture Patterns**: How components interact, data flow patterns
- **Error Handling**: Consistent error handling approaches
- **State Management**: How application state is managed
- **API Design**: RESTful conventions, GraphQL usage, authentication patterns

**Memory Creation:**
```json
{
  "type": "implementation-pattern",
  "pattern_name": "component-organization",
  "pattern_type": "code-structure",
  "technology_context": ["react", "typescript"],
  "pattern_description": "feature-based-folder-structure-with-colocation",
  "usage_frequency": "consistent-throughout-project",
  "effectiveness": "high-based-on-maintenance",
  "examples": ["src/features/auth/", "src/features/dashboard/"],
  "related_patterns": ["state-management", "routing"]
}
```

#### 3.2 Workflow Pattern Recognition
**Extract:**
- **Development Workflow**: Git flow, branching strategy, review process
- **Deployment Patterns**: CI/CD pipeline, staging/production flow
- **Testing Workflow**: When tests are written, how they're run
- **Documentation Patterns**: How decisions are documented, code documentation style

### Phase 4: Issue/Solution Mapping

#### 4.1 Technical Debt Documentation
**Identify:**
- **Performance Issues**: Known bottlenecks and their current status
- **Security Concerns**: Known vulnerabilities and mitigation status
- **Scalability Limitations**: Current limitations and planned solutions
- **Maintenance Burden**: Areas requiring frequent fixes

**Memory Creation:**
```json
{
  "type": "problem-solution",
  "domain": "performance",
  "problem": "slow-initial-page-load",
  "current_solution": "code-splitting-implemented",
  "effectiveness": "70-percent-improvement",
  "remaining_issues": ["image-optimization-needed"],
  "solution_stability": "stable-for-6-months",
  "maintenance_notes": "requires-bundle-analysis-monitoring"
}
```

#### 4.2 Common Debugging Solutions
**Extract:**
- **Frequent Issues**: Common bugs and their standard fixes
- **Environment Issues**: Development setup problems and solutions
- **Integration Challenges**: Third-party service issues and workarounds

### Phase 5: Preference & Style Inference

#### 5.1 Coding Style Analysis & Extraction
**CRITICAL**: Extract and document coding conventions for automatic style consistency

**Analyze Codebase for Style Patterns:**

**Naming Conventions:**
- **Variables**: camelCase, snake_case, PascalCase patterns
- **Functions**: Naming patterns (get*, set*, handle*, process*, validate*)
- **Classes**: Noun patterns, interface naming (I*, *Interface, *Impl)
- **Files**: kebab-case, PascalCase, index patterns
- **Constants**: SCREAMING_SNAKE_CASE, camelCase patterns

**Code Structure:**
- **Import Organization**: Grouped by type, alphabetical, relative vs absolute
- **Function Length**: Average length, maximum acceptable
- **Class Organization**: Constructor first, private methods last, etc.
- **Comment Style**: JSDoc, inline, block comment patterns
- **Error Handling**: try/catch patterns, error throwing conventions

**Formatting Preferences:**
- **Indentation**: Spaces vs tabs, indent size
- **Line Length**: Maximum characters per line
- **Bracket Style**: Same line vs new line for opening braces
- **Semicolon Usage**: Always, never, or ASI
- **Quote Style**: Single quotes, double quotes, template literals
- **Trailing Commas**: Always, never, multiline only

**Language-Specific Patterns:**

*JavaScript/TypeScript:*
- Function declaration vs arrow functions
- Async/await vs Promise chains
- Interface vs type aliases
- Destructuring patterns
- Optional chaining usage

*Python:*
- Function definitions and docstring style
- Class method organization
- Import statement organization
- List comprehension vs loops

*Other Languages:*
- Access modifier patterns
- Generic usage conventions
- Package/module organization

**Memory Creation for Style Rules:**
```json
{
  "type": "coding-style",
  "language": "typescript",
  "style_category": "naming-conventions",
  "rules": {
    "variables": "camelCase",
    "functions": "camelCase-with-verb-prefix",
    "classes": "PascalCase-nouns",
    "interfaces": "PascalCase-with-I-prefix",
    "files": "kebab-case-descriptive",
    "constants": "SCREAMING_SNAKE_CASE"
  },
  "evidence_files": ["src/utils/apiClient.ts", "src/components/UserList.tsx"],
  "consistency_score": 0.92,
  "project_context": "react-typescript-enterprise"
}
```

```json
{
  "type": "coding-style",
  "language": "typescript",
  "style_category": "formatting",
  "rules": {
    "indentation": "2-spaces",
    "line_length": "100-characters",
    "bracket_style": "same-line",
    "semicolons": "always",
    "quotes": "single-quotes",
    "trailing_commas": "multiline-only"
  },
  "evidence": "analyzed-50-files-consistent-pattern",
  "consistency_score": 0.95,
  "enforcement_tools": [".eslintrc.js", ".prettierrc"]
}
```

```json
{
  "type": "coding-style",
  "language": "typescript",
  "style_category": "code-organization",
  "rules": {
    "import_order": "external-then-internal-then-relative",
    "function_length": "max-30-lines-typical-15",
    "class_organization": "constructor-public-private-static",
    "comment_style": "jsdoc-for-public-inline-for-complex",
    "error_handling": "specific-errors-with-context"
  },
  "architectural_patterns": ["dependency-injection", "factory-pattern"],
  "consistency_score": 0.88
}
```

**Automatic Style Rule Generation:**
After analysis, create a style guide template populated with discovered patterns:
- Save to `.bmad/project/style-guide.md`
- Include examples from actual codebase
- Note consistency scores and exceptions
- Provide linter/formatter configurations

#### 5.2 Team Working Style Analysis
**Infer from Project:**
- **Documentation Preference**: Detailed vs minimal, inline vs external
- **Code Style**: Verbose vs concise, functional vs OOP preference
- **Decision Making**: Collaborative vs individual, documented vs verbal
- **Risk Tolerance**: Conservative vs experimental technology choices

**Questions for User:**
1. "Do you prefer detailed technical explanations or high-level summaries?"
2. "When making technical decisions, do you like to see alternatives and trade-offs?"
3. "How do you prefer to receive recommendations - with examples or just descriptions?"
4. "Do you like to validate each step or prefer to see larger blocks of work completed?"

**Memory Creation:**
```json
{
  "type": "user-preference",
  "preference_category": "communication-style",
  "preference": "detailed-technical-explanations",
  "evidence": ["comprehensive-documentation", "detailed-commit-messages"],
  "confidence": 0.8,
  "project_context": "brownfield-analysis",
  "adaptations": ["provide-implementation-examples", "include-alternative-approaches"]
}
```

## Bootstrap Execution Strategy

### Interactive Bootstrap Mode
**User Command**: `/bootstrap-memory --interactive`

**Process:**
1. **Guided Analysis**: Ask user to confirm findings at each phase
2. **Collaborative Memory Creation**: User validates and enhances extracted information
3. **Priority Setting**: User identifies most important patterns and decisions
4. **Customization**: Adapt memory entries based on user feedback

### Automated Bootstrap Mode  
**User Command**: `/bootstrap-memory --auto`

**Process:**
1. **Silent Analysis**: Automatically scan and analyze project artifacts
2. **Confidence Scoring**: Assign confidence levels to extracted information
3. **Bulk Memory Creation**: Create comprehensive memory entries
4. **Summary Report**: Present findings and allow user to validate/refine

### Focused Bootstrap Mode
**User Command**: `/bootstrap-memory --focus=architecture` (or `decisions`, `patterns`, `issues`)

**Process:**
1. **Targeted Analysis**: Focus on specific aspect of project
2. **Deep Dive**: More thorough analysis in chosen area
3. **Specialized Memory Creation**: Create detailed memories for focus area

## Memory Categories for Brownfield Bootstrap

### Essential Memories (Always Create)
1. **Project Context Memory**: Overall project understanding
2. **Technology Stack Memory**: Current technical foundation
3. **Architecture Decision Memory**: Key structural decisions
4. **User Preference Memory**: Working style and communication preferences

### High-Value Memories (Create When Found)
1. **Successful Pattern Memories**: Proven approaches in current project
2. **Problem-Solution Memories**: Known issues and their fixes
3. **Workflow Pattern Memories**: Effective development processes
4. **Performance Optimization Memories**: Successful performance improvements

### Nice-to-Have Memories (Create When Clear)
1. **Team Collaboration Memories**: Effective team working patterns
2. **Deployment Pattern Memories**: Successful deployment approaches
3. **Testing Strategy Memories**: Effective testing patterns
4. **Documentation Pattern Memories**: Successful documentation approaches

## Bootstrap Output

### Memory Bootstrap Report
Save the bootstrap report at `.bmad/history/bootstrap-reports/bootstrap-{timestamp}.md`:

```markdown
# 🧠 Memory Bootstrap Complete for {Project Name}

## Bootstrap Summary
**Analysis Duration**: {time-taken}
**Memories Created**: {total-count}
**Confidence Level**: {average-confidence}
**Report Location**: .bmad/history/bootstrap-reports/bootstrap-{timestamp}.md

## Memory Categories Created
- **Project Context**: {count} memories
- **Technical Decisions**: {count} memories  
- **Implementation Patterns**: {count} memories
- **Problem-Solutions**: {count} memories
- **User Preferences**: {count} memories

## Key Insights Discovered
### Successful Patterns Identified
- {pattern-1}: {confidence-level}
- {pattern-2}: {confidence-level}

### Critical Decisions Documented
- {decision-1}: {rationale-summary}
- {decision-2}: {rationale-summary}

### Optimization Opportunities
- {opportunity-1}: {potential-impact}
- {opportunity-2}: {potential-impact}

## Next Steps Recommended
1. **Immediate**: {recommended-next-action}
2. **Short-term**: {suggested-improvements}
3. **Long-term**: {strategic-opportunities}

## Memory Enhancement Opportunities
- [ ] Validate extracted decisions with team
- [ ] Add missing context to high-value patterns  
- [ ] Document recent changes and their outcomes
- [ ] Establish ongoing memory creation workflow

## Report Storage
- **Bootstrap Report**: `.bmad/history/bootstrap-reports/bootstrap-{timestamp}.md`
- **Memory Fallbacks**: `.bmad/system/memory/fallbacks/` (if memory system unavailable)
- **Follow-up Actions**: Track in `.bmad/current/analysis/bootstrap-followup.md`
```

### Validation Questions for User
```markdown
## 🔍 Bootstrap Validation

Please review these key findings:

### Technical Stack Assessment
**Identified**: {tech-stack}
**Confidence**: {confidence}%
**Question**: Does this accurately reflect your current technology choices?

### Architecture Pattern Recognition  
**Identified**: {architecture-pattern}
**Confidence**: {confidence}%
**Question**: Is this how you'd describe your current architecture approach?

### Working Style Inference
**Identified**: {working-style-patterns}
**Question**: Does this match your preferred working style and communication approach?

### Priority Validation
**High Priority Patterns**: {extracted-priorities}
**Question**: Are these the most important patterns to preserve and build upon?
```

## Integration with Existing BMAD Workflow

### After Bootstrap Completion
1. **Context-Rich Persona Activation**: All subsequent persona activations include bootstrap memory context
2. **Pattern-Informed Decision Making**: New decisions reference established patterns and previous choices
3. **Proactive Issue Prevention**: Known issues and solutions inform preventive measures
4. **Workflow Optimization**: Established patterns guide workflow recommendations

### Continuous Memory Enhancement
- **Decision Tracking**: New decisions add to established decision context
- **Pattern Refinement**: Successful outcomes refine existing pattern memories
- **Issue Resolution**: New solutions enhance problem-solution memories
- **Preference Learning**: User interactions refine preference memories

This bootstrap approach transforms a memory-enhanced BMAD system from "starting from scratch" to "building on existing intelligence" in 45-60 minutes of focused analysis.