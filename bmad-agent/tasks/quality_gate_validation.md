# Quality Gate Validation Task

## Purpose
Validate that all quality standards and patterns are met before proceeding to next phase through automated checks and phase-specific configurations. Store validation results at `.bmad/quality/validations/gate-results-{date}.md`.

## Automatic Trigger Points
Quality gates are automatically triggered at:
- **Phase Completion**: When completing any workflow phase
- **Story Completion**: When marking a story as done
- **Pre-Commit**: Before committing code changes
- **Pre-Merge**: Before merging to main branch
- **Milestone Reached**: At 25%, 50%, 75%, 100% completion
- **Critical Change**: When modifying architecture or security components

## Structured Thinking Validation (MANDATORY FIRST CHECK)

### Analysis Tag Verification
Before ANY gate validation proceeds:
- [ ] **Required Analysis Tag Present**: Appropriate tag for work type
- [ ] **All Sections Complete**: No missing mandatory sections
- [ ] **Evidence Provided**: Each section backed by data
- [ ] **Quality Score ≥85%**: Calculated from completeness/clarity
- [ ] **Confidence Level Stated**: With supporting factors

**GATE BLOCKED** if analysis tag missing or incomplete. Penalty: -$2000

### Valid Analysis Tags by Work Type:
- **Architecture Work**: `<architecture_analysis>` required
- **Feature Decisions**: `<decision_analysis>` required  
- **Bug Fixes**: `<problem_analysis>` required
- **Code Reviews**: `<quality_analysis>` required
- **Production Changes**: `<risk_analysis>` required

## Phase-Specific Gate Configurations

### Discovery Phase Gates
**Enforcement Level**: Standard
**Automatic Checks**:
- [ ] **Context Loaded**: Previous context restored if available
- [ ] **Memory Ready**: Memory system initialized
- [ ] **Problem Validation**: Problem clearly defined with evidence (≥90%)
- [ ] **User Research**: Target users researched and documented (≥85%)
- [ ] **Scope Definition**: Scope boundaries clearly established (≥95%)

### Requirements Phase Gates
**Enforcement Level**: Strict
**Automatic Checks**:
- [ ] **Discovery Complete**: Discovery phase gates passed
- [ ] **PRD Completeness**: PRD complete with all sections (≥95%)
- [ ] **Acceptance Criteria**: All stories have clear acceptance criteria (100%)
- [ ] **UI Specification**: UI flows and wireframes documented (≥90%)
- [ ] **Technical Feasibility**: Technical assumptions validated (≥85%)

### Architecture Phase Gates
**Enforcement Level**: Strict
**Automatic Checks**:
- [ ] **Requirements Complete**: Requirements phase gates passed
- [ ] **Architecture Analysis**: Architecture analysis tag present and complete (100%)
- [ ] **Scalability Design**: Scalability considerations documented (≥90%)
- [ ] **Security Architecture**: Security patterns implemented (≥95%)
- [ ] **Performance Planning**: Performance targets defined (≥85%)
- [ ] **Component Boundaries**: Clear module separation (≥95%)

### Development Phase Gates
**Enforcement Level**: Strict

#### Pre-Commit Gate (Automatic)
- [ ] **Linting**: Zero linting violations (100%)
- [ ] **Type Checking**: Zero type errors (100%)
- [ ] **Unit Tests**: All unit tests passing (100%)
- [ ] **Style Consistency**: Code matches project style patterns (≥95%)

#### Story Completion Gate (Automatic)
- [ ] **DoD Checklist**: Definition of Done complete (100%)
- [ ] **Test Coverage**: Minimum test coverage met (≥85%)
- [ ] **Code Review**: Code review approved (100%)
- [ ] **Integration Tests**: Integration tests passing (100%)

#### Sprint End Gate
- [ ] **Sprint Goals**: Sprint goals achieved (≥90%)
- [ ] **Technical Debt**: Technical debt within limits (≥85%)
- [ ] **Performance Baseline**: Performance metrics maintained (≥95%)

## Anti-Pattern Check
Fail immediately if any of these are detected:
- Mock services in production paths
- Placeholder implementations (TODO, FIXME, pass)
- Dummy data instead of real processing
- Generic exception handling
- Assumption-based solutions without verification

## Gate Enforcement Protocol

### Automatic Gate Execution
```python
def execute_quality_gate(trigger_point, context):
    """Automatically execute quality gate based on trigger"""
    
    # Load phase-specific configuration
    phase_config = load_phase_config(context.current_phase)
    gate_config = load_gate_config(trigger_point)
    
    # Run automated checks
    results = run_automated_checks(gate_config.checks)
    
    # Evaluate against thresholds
    gate_passed = evaluate_results(results, gate_config.thresholds)
    
    # Generate improvement guidance if failed
    if not gate_passed:
        improvements = generate_improvement_guidance(results, context)
        return GateResult(passed=False, improvements=improvements)
    
    return GateResult(passed=True)
```

### Gate Failure Response
1. **IMMEDIATE STOP**: Halt all work on current task
2. **ROOT CAUSE ANALYSIS**: Identify why gate failed
3. **IMPROVEMENT GUIDANCE**: Receive memory-based suggestions
4. **CORRECTIVE ACTION**: Address underlying issues
5. **RE-VALIDATION**: Repeat gate check after fixes
6. **DOCUMENTATION**: Record lessons learned

### Override Mechanism (Phase-Specific)
**Minor Override** (Advisory gates only):
- Approval: Tech Lead
- Documentation: Justification + risk assessment
- Timeline: Fix within 48 hours

**Major Override** (Standard enforcement):
- Approval: Architect
- Documentation: Business justification + mitigation plan
- Timeline: Fix within sprint

**Critical Override** (Strict enforcement):
- Approval: Project Manager + Architect
- Documentation: Executive justification + full risk analysis
- Timeline: Immediate remediation plan
- Accountability: Named individual responsible

## Output
- **PASS**: All gates satisfied, proceed to next phase
- **CONDITIONAL**: Minor issues requiring fixes, timeline < 1 day
- **FAIL**: Major issues, return to planning phase

## Success Criteria
All quality gates pass with documented evidence and peer validation. Results documented and stored for tracking.

## Improvement Guidance System

### Automatic Improvement Suggestions
When a gate fails, the system automatically provides:

```yaml
improvement_guidance:
  source_priority:
    1: "memory_patterns"      # What worked in similar situations
    2: "team_history"        # How this team solved it before
    3: "best_practices"      # Industry standard solutions
    4: "similar_projects"    # Solutions from comparable projects
  
  suggestion_format:
    problem: "Specific issue identified"
    root_cause: "Why this happened"
    immediate_action: "Quick fix to unblock"
    proper_solution: "Long-term fix"
    prevention: "How to avoid in future"
    examples: "Links to similar solutions"
```

### Memory-Based Pattern Matching
```python
def generate_improvement_guidance(gate_failure, context):
    """Generate improvement suggestions from memory"""
    
    # Search memory for similar failures
    similar_failures = memory.search(f"gate failure {gate_failure.type}")
    
    # Find successful resolutions
    resolutions = memory.search(f"resolved {gate_failure.type}")
    
    # Generate guidance
    guidance = {
        "immediate_fixes": extract_quick_fixes(resolutions),
        "best_practices": find_best_practices(gate_failure.type),
        "team_patterns": get_team_success_patterns(context.team),
        "estimated_time": calculate_resolution_time(similar_failures)
    }
    
    return format_guidance(guidance)
```

## Gate Metrics
Track and report:
- Gate pass/fail rates by phase
- Average time to resolve gate failures
- Most common gate failure reasons
- Quality trend over time
- Override frequency and justifications
- Improvement effectiveness

## Integration Points
- **Story Completion**: All gates must pass before story marked done
- **Sprint Planning**: Gate history influences complexity estimates
- **Release Planning**: Gate metrics inform release readiness
- **Retrospectives**: Gate failures analyzed for process improvement
- **Documentation**: All validation results stored at `.bmad/quality/validations/gate-results-{date}.md`
- **Tracking**: Gate metrics and trends maintained at `.bmad/quality/diagnostics/gate-metrics.md`

## Output Deliverables
- **Primary Report**: Gate validation results at `.bmad/quality/validations/gate-results-{date}.md`
- **Metrics Update**: Gate performance metrics at `.bmad/quality/diagnostics/gate-metrics.md`
- **Action Items**: Any required fixes tracked in current work items