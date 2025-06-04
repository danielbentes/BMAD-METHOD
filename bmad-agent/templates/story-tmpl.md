# Story {EpicNum}.{StoryNum}: {Short Title Copied from Epic File}

## Status: { Draft | Approved | InProgress | Review | Done }
**Quality Gate**: { NotStarted | 25% | 50% | 75% | 100% }

## Story Justification & Evidence

### Business Value Evidence
- **Problem Statement**: {Clear description of the problem being solved}
- **Value Metrics**: {Quantifiable benefits - time saved, efficiency gained, etc.}
- **User Research**: {Reference to user feedback, analytics, or research}
- **Priority Score**: {High/Medium/Low with justification}

### Technical Feasibility Evidence
- **Architecture Alignment**: {How this fits into system architecture}
- **Technical Risk Assessment**: {Low/Medium/High with mitigation plan}
- **Proof of Concept**: {Link to POC or spike results if applicable}
- **Performance Impact**: {Expected impact on system performance}

## Story

- As a [role]
- I want [action]
- so that [benefit]

### Story Validation Checklist
- [ ] User role is clearly defined and exists in system
- [ ] Action is specific and achievable
- [ ] Benefit is measurable and aligns with epic goals
- [ ] Story is independent and deliverable in one sprint
- [ ] Story follows INVEST principles

## Acceptance Criteria (ACs) with Validation

### AC Validation Framework
Each AC must include:
1. **Given** (precondition with evidence)
2. **When** (action with clear trigger)
3. **Then** (outcome with measurable result)
4. **Evidence** (how we verify this AC)

### Acceptance Criteria
1. **AC1**: {Description}
   - Given: {Precondition}
   - When: {Action}
   - Then: {Expected outcome}
   - Evidence: {Test data, scenarios, or validation method}
   - Test Coverage: {Unit/Integration/E2E}

2. **AC2**: {Description}
   - Given: {Precondition}
   - When: {Action}
   - Then: {Expected outcome}
   - Evidence: {Test data, scenarios, or validation method}
   - Test Coverage: {Unit/Integration/E2E}

### Testability Requirements
- **Test Data Requirements**: {Specific data needed for testing}
- **Test Environment**: {Environment specifications}
- **Automated Test Coverage**: {Target percentage and types}
- **Manual Test Scenarios**: {Critical user paths requiring manual validation}
- **Performance Benchmarks**: {Response time, throughput requirements}

## Dependencies & Validation

### Upstream Dependencies
| Dependency | Type | Status | Evidence | Risk |
|------------|------|--------|----------|------|
| {System/Story/API} | {Technical/Data/Business} | {Ready/InProgress/Blocked} | {Link/Reference} | {Low/Med/High} |

### Downstream Impact
| Affected System | Impact Type | Notification Status | Evidence |
|-----------------|-------------|-------------------|----------|
| {System/Feature} | {Breaking/Non-breaking} | {Notified/Pending} | {Communication link} |

### Dependency Validation Checklist
- [ ] All dependencies identified and documented
- [ ] Dependency owners notified and acknowledged
- [ ] Fallback plan exists for critical dependencies
- [ ] Integration points clearly defined

## Estimation & Accuracy Tracking

### Initial Estimation
- **Story Points**: {Points with justification}
- **Estimation Method**: {Planning Poker/T-Shirt/Affinity}
- **Confidence Level**: {High/Medium/Low}
- **Assumptions**: {List key assumptions affecting estimate}

### Estimation Evidence
- **Similar Stories**: {Reference to comparable completed stories}
- **Technical Complexity**: {Simple/Moderate/Complex with reasoning}
- **Team Velocity**: {Historical velocity for similar work}
- **Risk Factors**: {Factors that could impact estimate}

### Actual vs Estimated (Post-Implementation)
- **Actual Story Points**: {Actual effort}
- **Variance**: {Percentage over/under}
- **Variance Reasons**: {Why estimate was off}
- **Lessons Learned**: {What to improve in future estimations}

## Tasks / Subtasks with Evidence

### Task Breakdown Validation
- [ ] Each task maps to specific AC(s)
- [ ] Tasks are independently testable
- [ ] Task dependencies are identified
- [ ] Time estimates provided for each task

### Tasks
- [ ] **Task 1**: {Description} (AC: #1)
  - **Evidence Required**: {What proves this task is complete}
  - **Estimated Hours**: {Hours}
  - **Acceptance Test**: {How to verify completion}
  - [ ] Subtask 1.1: {Description}
  - [ ] Subtask 1.2: {Description}

- [ ] **Task 2**: {Description} (AC: #2)
  - **Evidence Required**: {What proves this task is complete}
  - **Estimated Hours**: {Hours}
  - **Acceptance Test**: {How to verify completion}
  - [ ] Subtask 2.1: {Description}
  - [ ] Subtask 2.2: {Description}

## Quality Gate Checkpoints

### 25% Checkpoint
- [ ] Story justification reviewed and approved
- [ ] Dependencies validated and confirmed
- [ ] Technical approach documented
- [ ] Test strategy defined
- **Evidence**: {Links to reviews/approvals}

### 50% Checkpoint
- [ ] Core functionality implemented
- [ ] Unit tests passing
- [ ] No critical blockers
- [ ] On track for estimation
- **Evidence**: {Test results, code coverage}

### 75% Checkpoint
- [ ] All ACs implemented
- [ ] Integration tests passing
- [ ] Code review completed
- [ ] Documentation updated
- **Evidence**: {PR links, test reports}

### 100% Checkpoint
- [ ] All tests passing (Unit, Integration, E2E)
- [ ] Performance benchmarks met
- [ ] Security review completed
- [ ] Deployment ready
- **Evidence**: {Final test results, approvals}

## Dev Technical Guidance

### Implementation Approach
- **Architecture Pattern**: {Pattern to follow with justification}
- **Key Technical Decisions**: {Decisions with evidence/reasoning}
- **Code Quality Standards**: {Specific standards to maintain}
- **Performance Considerations**: {Specific optimizations needed}

### Technical Evidence Requirements
- [ ] Code follows established patterns
- [ ] Error handling comprehensive
- [ ] Logging sufficient for debugging
- [ ] Security best practices applied
- [ ] Performance optimized

## Post-Implementation Validation

### Definition of Done Checklist
- [ ] All ACs met with evidence
- [ ] Code reviewed and approved
- [ ] Tests automated and passing
- [ ] Documentation complete
- [ ] Performance validated
- [ ] Security validated
- [ ] Deployed to staging
- [ ] Product owner accepted

### Success Metrics (Post-Deployment)
- **Metric 1**: {What to measure} - Target: {Value}
- **Metric 2**: {What to measure} - Target: {Value}
- **Measurement Period**: {How long to track}
- **Success Criteria**: {What defines success}

### Post-Implementation Review
- **Delivery Date**: {Actual completion date}
- **Total Effort**: {Actual hours/points}
- **Quality Metrics**: {Defects found, test coverage achieved}
- **Stakeholder Feedback**: {Summary of feedback received}
- **Process Improvements**: {What to do better next time}

## Story Progress Notes

### Agent Model Used: `<Agent Model Name/Version>`

### Implementation Evidence Log
| Date | Milestone | Evidence | Reviewer |
|------|-----------|----------|----------|
| {Date} | {What was completed} | {Link/Reference} | {Who reviewed} |

### Risk & Issue Log
| Date | Type | Description | Impact | Resolution | Evidence |
|------|------|-------------|---------|------------|----------|
| {Date} | {Risk/Issue} | {Description} | {High/Med/Low} | {Action taken} | {Link} |

### Decision Log
| Date | Decision | Rationale | Evidence | Approver |
|------|----------|-----------|----------|----------|
| {Date} | {What was decided} | {Why} | {Supporting data} | {Who approved} |

### Change Log
| Date | Change Type | Description | Reason | Impact Assessment | Approval |
|------|-------------|-------------|---------|------------------|----------|
| {Date} | {Scope/Technical/Timeline} | {What changed} | {Why} | {Impact analysis} | {Approver} |

---

## Quality Enforcement Notice
This story must pass all quality gates and provide evidence at each checkpoint. Any deviation from evidence requirements must be documented with justification and risk assessment.
