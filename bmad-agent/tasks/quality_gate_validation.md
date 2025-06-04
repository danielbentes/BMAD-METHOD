# Quality Gate Validation Task

## Purpose
Validate that all quality standards and patterns are met before proceeding to next phase. Store validation results at `.bmad/quality/validations/gate-results-{date}.md`.

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

## Pre-Implementation Gate
- [ ] **Planning Complete**: Comprehensive plan documented
- [ ] **Context Gathered**: All necessary information collected
- [ ] **UDTM Executed**: Ultra-deep thinking mode completed
- [ ] **Assumptions Challenged**: All assumptions explicitly verified
- [ ] **Root Cause Identified**: For any existing issues
- [ ] **Analysis Tag Validated**: Structured thinking enforced

## Implementation Gate
- [ ] **Real Implementation**: No mocks, stubs, or placeholders
- [ ] **Code Quality**: 0 Ruff violations, 0 MyPy errors
- [ ] **Integration Testing**: Works with existing components
- [ ] **Error Handling**: Specific exceptions with proper context
- [ ] **Documentation**: All functions/classes properly documented

## Completion Gate
- [ ] **Functionality Verified**: Actually works as specified
- [ ] **Tests Pass**: All tests verify real functionality
- [ ] **Performance Acceptable**: Meets performance requirements
- [ ] **Security Reviewed**: No obvious vulnerabilities
- [ ] **Brotherhood Review**: Peer validation completed

## Anti-Pattern Check
Fail immediately if any of these are detected:
- Mock services in production paths
- Placeholder implementations (TODO, FIXME, pass)
- Dummy data instead of real processing
- Generic exception handling
- Assumption-based solutions without verification

## Gate Enforcement Protocol

### Gate Failure Response
1. **IMMEDIATE STOP**: Halt all work on current task
2. **ROOT CAUSE ANALYSIS**: Identify why gate failed
3. **CORRECTIVE ACTION**: Address underlying issues
4. **RE-VALIDATION**: Repeat gate check after fixes
5. **DOCUMENTATION**: Record lessons learned

### Gate Override (Emergency Only)
- Requires explicit approval from project lead
- Must document business justification
- Technical debt ticket must be created
- Timeline for proper resolution required

## Output
- **PASS**: All gates satisfied, proceed to next phase
- **CONDITIONAL**: Minor issues requiring fixes, timeline < 1 day
- **FAIL**: Major issues, return to planning phase

## Success Criteria
All quality gates pass with documented evidence and peer validation. Results documented and stored for tracking.

## Gate Metrics
Track and report:
- Gate pass/fail rates by phase
- Average time to resolve gate failures
- Most common gate failure reasons
- Quality trend over time

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