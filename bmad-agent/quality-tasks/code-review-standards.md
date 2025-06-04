# CRITICAL TASK: Code Review Standards - Zero Defect Enforcement

## CRITICAL SAFETY RULES (MANDATORY COMPLIANCE)

### RULE 0 (MOST IMPORTANT): Review Blocking Protocol
If ANY critical issue is found, you MUST:
1. **BLOCK** the merge immediately
2. **TAG** as "Requires Changes" with no exceptions
3. **DOCUMENT** each issue with specific line numbers
4. **REQUIRE** complete fix (not workarounds)
5. **RE-REVIEW** entire changeset after fixes

**PENALTY**: Approving code with critical issues = -$3000 penalty + production incident risk + mandatory review training

### RULE 1: Zero Tolerance Issues
**NEVER APPROVE** code containing:
- Security vulnerabilities (any severity)
- Hardcoded secrets or credentials
- SQL injection possibilities
- Memory leaks or resource exhaustion
- Data loss scenarios
- Performance degradations >10%
- Accessibility violations

### RULE 2: Code Quality Standards
**ALL** code MUST demonstrate:
- Clear intent and readability
- Proper error handling (no silent failures)
- Comprehensive test coverage (>80%)
- No code duplication (DRY principle)
- SOLID principles adherence
- Consistent style guide compliance

### RULE 3: Review Completeness
**EVERY** review MUST examine:
- Business logic correctness
- Edge case handling
- Security implications
- Performance impact
- Test coverage adequacy
- Documentation accuracy

### RULE 4: Review Timeliness
**NO DELAYS** permitted for:
- Critical fixes: Review within 1 hour
- Security patches: Review within 2 hours
- Normal changes: Review within 4 hours
- Large changes: Initial feedback within 8 hours

### RULE 5: Reviewer Accountability
**ALL** reviewers are responsible for:
- Defects missed in review
- Security issues not caught
- Performance problems overlooked
- Anti-patterns approved
- Standards violations passed

## PURPOSE (MANDATORY UNDERSTANDING)
Enforce rigorous code review standards to catch defects before production, maintain code quality, share knowledge, and prevent technical debt accumulation. Code review is the LAST line of defense.

## REVIEW PHASES (PROGRESSIVE DISCLOSURE)

### Phase 1: Automated Pre-Review (IMMEDIATE)
**Time: Before human review assignment**

**Automated Checks (ALL MUST PASS):**
```yaml
pre_review_gates:
  - build_status: SUCCESS
  - test_coverage: ">80%"
  - linting_errors: ZERO
  - security_scan: NO_VULNERABILITIES
  - complexity_check: "<10"
  - duplication_check: "<3%"
```

**Auto-Rejection Triggers:**
- Build failure
- Test coverage <70%
- Critical security findings
- Merge conflicts present
- Files >500 lines changed without justification

**Review Assignment Logic:**
```python
def assign_reviewer(pr):
    if pr.touches_security():
        return security_team_member
    elif pr.touches_architecture():
        return senior_architect
    elif pr.is_critical_fix():
        return on_call_senior
    else:
        return team_member_with_context
```

**PHASE 1 GATE**: No human review if automated checks fail

### Phase 2: Review Assignment & SLA (STRICT TIMING)
**Time: Based on change criticality**

**Priority Classification:**
```yaml
review_priority:
  CRITICAL:
    - security_fixes
    - data_loss_bugs
    - system_down_issues
    SLA: 1_hour
    
  HIGH:
    - performance_issues
    - customer_facing_bugs
    - integration_problems
    SLA: 4_hours
    
  NORMAL:
    - feature_development
    - refactoring
    - documentation
    SLA: 8_hours
    
  LOW:
    - cosmetic_changes
    - test_additions
    - comment_updates
    SLA: 24_hours
```

**Escalation Protocol:**
```
IF review_not_started_by(SLA * 0.5):
    notify_reviewer()
IF review_not_started_by(SLA * 0.75):
    notify_team_lead()
IF review_not_started_by(SLA):
    escalate_to_manager()
    assign_backup_reviewer()
```

**PHASE 2 GATE**: Review must start within SLA

### Phase 3: Deep Review Execution (COMPREHENSIVE)
**Time: Proportional to change size**

**Review Checklist - Business Logic:**
- [ ] Requirements correctly implemented
- [ ] Edge cases handled properly
- [ ] Business rules enforced
- [ ] Data validation complete
- [ ] User experience considered

**Review Checklist - Code Quality:**
- [ ] Code is self-documenting
- [ ] No magic numbers/strings
- [ ] Proper abstraction levels
- [ ] DRY principle followed
- [ ] SOLID principles applied

**Review Checklist - Security:**
- [ ] Input validation present
- [ ] Output encoding implemented
- [ ] Authentication checks proper
- [ ] Authorization enforced
- [ ] Sensitive data protected

**Review Checklist - Performance:**
- [ ] No N+1 queries
- [ ] Efficient algorithms used
- [ ] Caching implemented where needed
- [ ] Resource cleanup proper
- [ ] Async where appropriate

**Review Checklist - Testing:**
- [ ] Unit tests comprehensive
- [ ] Integration tests present
- [ ] Edge cases tested
- [ ] Error scenarios covered
- [ ] Performance tests added

**Comment Classification:**
```markdown
[BLOCKER]: Must fix before merge (security, data loss, crashes)
[CRITICAL]: Must fix before merge (bugs, standards violations)
[MAJOR]: Should fix before merge (code quality, maintainability)
[MINOR]: Consider fixing (style, preferences)
[NITPICK]: Optional improvements
[QUESTION]: Needs clarification
[PRAISE]: Good practices to reinforce
```

**PHASE 3 GATE**: All BLOCKER and CRITICAL issues resolved

### Phase 4: Feedback & Resolution (ENFORCEMENT)
**Time: Until all issues resolved**

**Author Response Requirements:**
- Acknowledge within 4 hours
- Fix or justify each comment
- Update PR description with changes
- Request re-review explicitly
- No force-pushing after review starts

**Re-Review Protocol:**
```yaml
re_review_triggers:
  - blocker_issues_fixed: FULL_RE_REVIEW
  - critical_issues_fixed: TARGETED_RE_REVIEW
  - major_changes_made: FULL_RE_REVIEW
  - merge_conflicts_resolved: CONFLICT_AREAS_ONLY
  - minor_updates: QUICK_VERIFICATION
```

**Approval Requirements:**
- All BLOCKER issues resolved
- All CRITICAL issues resolved
- 80% of MAJOR issues addressed
- No unresolved security concerns
- Tests still passing
- No new issues introduced

**PHASE 4 GATE**: Explicit approval with no outstanding blockers

## QUALITY GATES (MANDATORY CHECKPOINTS)

### Submission Gate
- [ ] PR description complete
- [ ] Linked to issue/story
- [ ] Tests included
- [ ] Self-review done
- [ ] No merge conflicts

### Automated Gate
- [ ] Build passing
- [ ] Tests passing
- [ ] Coverage adequate
- [ ] Security clean
- [ ] Lint clean

### Review Gate
- [ ] Reviewer assigned
- [ ] SLA met
- [ ] Checklist complete
- [ ] Issues documented
- [ ] Feedback provided

### Approval Gate
- [ ] All blockers resolved
- [ ] Re-review complete
- [ ] Final tests passing
- [ ] No regressions
- [ ] Ready to merge

## SUCCESS METRICS (MANDATORY TARGETS)

### Review Efficiency Metrics
- **Review start time**: <2 hours for critical
- **Review completion**: <24 hours average
- **First-pass approval rate**: >60%
- **Re-review cycles**: <2 average
- **SLA compliance**: >95%

### Review Quality Metrics
- **Defect detection rate**: >90%
- **Security issues caught**: 100%
- **Performance issues caught**: >85%
- **Post-merge defects**: <1 per 100 PRs
- **Review coverage**: 100% of changes

### Team Metrics
- **Reviewer participation**: 100%
- **Review load balance**: ±20%
- **Knowledge sharing**: >3 reviewers/week
- **Mentoring comments**: >10%
- **Positive feedback**: >20%

**METRIC FAILURE PENALTY**: Below targets trigger review process audit

## ERROR HANDLING PROTOCOLS

### When Critical Issues Missed
1. **IMMEDIATE** incident response
2. **ROOT CAUSE** analysis required
3. **REVIEWER** additional training
4. **PROCESS** improvement mandatory
5. **PREVENTION** measures implemented
6. **AUDIT** next 10 reviews

### When SLAs Missed
1. **ESCALATE** immediately
2. **ASSIGN** backup reviewer
3. **TRACK** miss reasons
4. **ADJUST** workload
5. **IMPROVE** assignment
6. **MONITOR** closely

### When Standards Violated
1. **BLOCK** the merge
2. **EDUCATE** the author
3. **DOCUMENT** the pattern
4. **UPDATE** automation
5. **SHARE** learnings
6. **PREVENT** recurrence

## REVIEWER ACCOUNTABILITY

### Performance Tracking
```yaml
reviewer_metrics:
  - reviews_completed_monthly
  - average_review_time
  - defects_missed_count
  - sla_compliance_rate
  - feedback_quality_score
  - mentoring_instances
```

### Accountability Matrix
| Missed Issue Type | First Instance | Second Instance | Third Instance |
|------------------|----------------|-----------------|----------------|
| Security | Warning + Training | Review audit | Review privilege suspension |
| Critical Bug | Discussion | Additional training | Paired reviews required |
| Performance | Coaching | Review checklist | Senior review required |
| Code Quality | Feedback | Process review | Mentoring assigned |

### Recognition System
- Monthly "Thorough Reviewer" award
- Defect prevention bonuses
- Knowledge sharing rewards
- Mentoring acknowledgments
- Quality feedback prizes

## ANTI-PATTERN DETECTION

### Code Anti-Patterns (ZERO TOLERANCE)
1. **God Objects**: Classes doing too much
2. **Copy-Paste**: Duplicated code blocks
3. **Magic Numbers**: Hardcoded values
4. **Long Methods**: >50 lines
5. **Deep Nesting**: >3 levels
6. **Poor Naming**: Unclear variables/functions
7. **Missing Error Handling**: Catch without action

### Review Anti-Patterns (MUST PREVENT)
1. **Rubber Stamping**: Approval without real review
2. **Nitpick Focus**: Missing forest for trees
3. **Style Wars**: Personal preference battles
4. **Delayed Reviews**: Sitting on PRs
5. **Harsh Feedback**: Demotivating comments
6. **Incomplete Reviews**: Partial examination

## CONTINUOUS IMPROVEMENT

### Weekly Analysis
- Review metrics dashboard
- Missed defect patterns
- SLA compliance trends
- Team feedback themes
- Process bottlenecks

### Monthly Improvements
- Update review checklists
- Enhance automation rules
- Refine assignment logic
- Adjust SLA targets
- Share best practices

### Quarterly Training
- Security review techniques
- Performance analysis skills
- Constructive feedback methods
- New tool adoption
- Anti-pattern recognition

## ENFORCEMENT MECHANISMS

### Automated Enforcement
```yaml
review_automation:
  pre_checks:
    - branch_protection_rules
    - required_review_count
    - dismiss_stale_reviews
    - require_up_to_date
    
  quality_checks:
    - minimum_coverage_increase
    - no_decrease_in_quality_metrics
    - security_scan_must_pass
    - performance_benchmark_met
    
  merge_protection:
    - no_admin_override
    - no_force_push
    - linear_history_required
    - signed_commits_only
```

### Manual Enforcement
- Review audit sampling (10% monthly)
- Peer review of reviews
- Manager oversight of metrics
- Team retrospectives on quality
- External audit quarterly

Remember: Code review is where quality is ensured or compromised. Every approved line of code is your responsibility. Review like the code will run in production forever—because it might. Be thorough, be kind, be uncompromising on standards.