# Quality Gate Check Task

## Purpose
Execute automated quality gate checks at predefined trigger points to ensure consistent quality throughout the development lifecycle. Provide real-time feedback and improvement guidance when gates fail.

## Behavioral Instructions

When a quality gate trigger occurs:

### 1. Automatic Trigger Detection

```python
def detect_quality_gate_trigger(event, context):
    """Detect when a quality gate should be executed"""
    
    trigger_map = {
        "commit_staged": "pre_commit",
        "story_marked_done": "story_completion",
        "phase_completed": "phase_exit",
        "pr_created": "pre_merge",
        "milestone_reached": "milestone_gate",
        "architecture_modified": "critical_change",
        "security_component_changed": "critical_change"
    }
    
    if event.type in trigger_map:
        return execute_gate_check(trigger_map[event.type], context)
```

### 2. Gate Configuration Loading

#### 2.1 Phase-Based Configuration
```yaml
phase_gate_configs:
  discovery:
    enforcement: "standard"
    automated_checks:
      - context_restoration: {required: true}
      - memory_initialization: {required: true}
      - problem_clarity: {threshold: 90}
      - user_research_depth: {threshold: 85}
      - scope_boundaries: {threshold: 95}
    manual_checks:
      - stakeholder_alignment
      - feasibility_assessment
      
  requirements:
    enforcement: "strict"
    automated_checks:
      - prd_sections_complete: {threshold: 95}
      - acceptance_criteria_clarity: {threshold: 100}
      - ui_specifications: {threshold: 90}
      - technical_assumptions: {threshold: 85}
    manual_checks:
      - user_story_quality
      - design_consistency
      
  architecture:
    enforcement: "strict"
    automated_checks:
      - architecture_analysis_tag: {required: true}
      - scalability_patterns: {threshold: 90}
      - security_implementation: {threshold: 95}
      - performance_targets: {threshold: 85}
      - component_separation: {threshold: 95}
    manual_checks:
      - udtm_completion
      - cross_team_review
      
  development:
    enforcement: "strict"
    automated_checks:
      - linting_violations: {threshold: 0}
      - type_errors: {threshold: 0}
      - test_coverage: {threshold: 85}
      - style_consistency: {threshold: 95}
      - complexity_metrics: {threshold: 10}
    manual_checks:
      - code_review_approval
      - integration_verification
```

#### 2.2 Trigger-Based Configuration
```yaml
trigger_gate_configs:
  pre_commit:
    enforcement: "strict"
    automated_percentage: 100
    checks:
      - linting_clean
      - types_valid
      - tests_passing
      - style_compliant
    failure_action: "block_commit"
    
  story_completion:
    enforcement: "strict"
    automated_percentage: 85
    checks:
      - dod_complete
      - tests_comprehensive
      - documentation_updated
      - code_reviewed
    failure_action: "block_story_closure"
    
  pre_merge:
    enforcement: "strict"
    automated_percentage: 90
    checks:
      - all_checks_passing
      - no_merge_conflicts
      - security_scan_clean
      - performance_baseline_met
    failure_action: "block_merge"
```

### 3. Automated Check Execution

#### 3.1 Check Runner Implementation
```python
def run_automated_checks(gate_config, context):
    """Execute all automated checks for the gate"""
    
    results = CheckResults()
    
    for check in gate_config.automated_checks:
        try:
            if check.type == "threshold":
                result = evaluate_threshold_check(check, context)
            elif check.type == "required":
                result = evaluate_required_check(check, context)
            elif check.type == "pattern":
                result = evaluate_pattern_check(check, context)
            
            results.add(check.name, result)
            
        except CheckException as e:
            results.add_error(check.name, str(e))
    
    return results
```

#### 3.2 Threshold Evaluation
```python
def evaluate_threshold_check(check, context):
    """Evaluate checks against numeric thresholds"""
    
    actual_value = measure_metric(check.metric, context)
    threshold = check.threshold
    
    if check.comparison == "minimum":
        passed = actual_value >= threshold
    elif check.comparison == "maximum":
        passed = actual_value <= threshold
    elif check.comparison == "exact":
        passed = actual_value == threshold
    
    return CheckResult(
        passed=passed,
        actual=actual_value,
        expected=threshold,
        message=f"{check.metric}: {actual_value} (threshold: {threshold})"
    )
```

### 4. Improvement Guidance Generation

#### 4.1 Memory-Based Suggestions
```python
def generate_improvement_guidance(failures, context):
    """Generate actionable improvement suggestions"""
    
    guidance = ImprovementGuidance()
    
    for failure in failures:
        # Search memory for similar issues
        similar_issues = memory.search(
            f"quality gate failure {failure.type} {failure.check_name}"
        )
        
        # Find successful resolutions
        resolutions = memory.search(
            f"resolved {failure.type} success pattern"
        )
        
        # Extract team-specific patterns
        team_patterns = memory.search(
            f"team:{context.team} {failure.type} resolution"
        )
        
        # Build guidance
        guidance.add_suggestion(
            failure=failure,
            immediate_fix=extract_quick_fix(resolutions),
            proper_solution=extract_best_practice(resolutions),
            team_approach=extract_team_pattern(team_patterns),
            estimated_time=calculate_resolution_time(similar_issues),
            examples=find_relevant_examples(failure.type)
        )
    
    return guidance
```

#### 4.2 Guidance Prioritization
```python
def prioritize_guidance(guidance, context):
    """Prioritize improvement suggestions by impact"""
    
    priorities = []
    
    for suggestion in guidance.suggestions:
        priority_score = calculate_priority(
            blocking_severity=suggestion.failure.severity,
            team_velocity_impact=estimate_velocity_impact(suggestion),
            fix_complexity=suggestion.estimated_time,
            risk_level=assess_risk(suggestion.failure)
        )
        
        priorities.append((priority_score, suggestion))
    
    # Sort by priority (highest first)
    priorities.sort(key=lambda x: x[0], reverse=True)
    
    return [suggestion for _, suggestion in priorities]
```

### 5. Gate Result Processing

#### 5.1 Result Evaluation
```python
def evaluate_gate_results(results, gate_config):
    """Determine if gate passes based on results"""
    
    gate_status = GateStatus()
    
    # Check critical failures
    critical_failures = [
        r for r in results 
        if r.check_name in gate_config.critical_checks and not r.passed
    ]
    
    if critical_failures:
        gate_status.passed = False
        gate_status.blocking_issues = critical_failures
        gate_status.can_override = gate_config.enforcement != "strict"
    else:
        # Check threshold compliance
        total_checks = len(results)
        passed_checks = len([r for r in results if r.passed])
        pass_percentage = (passed_checks / total_checks) * 100
        
        gate_status.passed = pass_percentage >= gate_config.minimum_pass_rate
        gate_status.score = pass_percentage
    
    return gate_status
```

#### 5.2 Enforcement Actions
```python
def enforce_gate_decision(gate_status, gate_config, context):
    """Take enforcement action based on gate results"""
    
    if gate_status.passed:
        log_gate_success(gate_status, context)
        allow_progress()
    else:
        if gate_config.enforcement == "strict":
            block_progress()
            notify_team(gate_status.blocking_issues)
            provide_improvement_guidance(gate_status.failures)
            require_fix_before_retry()
            
        elif gate_config.enforcement == "standard":
            flag_for_review()
            suggest_improvements(gate_status.failures)
            allow_conditional_progress()
            
        else:  # advisory
            log_warnings(gate_status.failures)
            track_technical_debt(gate_status.failures)
            allow_progress_with_warnings()
```

### 6. Override Handling

#### 6.1 Override Request Validation
```python
def handle_override_request(gate_name, justification, requester):
    """Process gate override request"""
    
    # Load gate configuration
    gate_config = load_gate_config(gate_name)
    
    # Check if override allowed
    if not gate_config.override_allowed:
        return OverrideResult(
            approved=False,
            reason="Gate does not allow overrides"
        )
    
    # Verify authority
    required_role = determine_required_authority(gate_config.enforcement)
    if not has_authority(requester, required_role):
        return OverrideResult(
            approved=False,
            reason=f"Requires {required_role} authority"
        )
    
    # Validate justification
    if not validate_justification(justification):
        return OverrideResult(
            approved=False,
            reason="Insufficient justification provided"
        )
    
    # Create accountability record
    create_override_record(
        gate=gate_name,
        requester=requester,
        justification=justification,
        timestamp=now(),
        remediation_required=True
    )
    
    return OverrideResult(approved=True)
```

### 7. Metrics Collection

#### 7.1 Gate Performance Tracking
```python
def track_gate_metrics(gate_name, gate_status, context):
    """Track quality gate performance metrics"""
    
    metrics = {
        "gate_name": gate_name,
        "phase": context.current_phase,
        "trigger": context.trigger_type,
        "timestamp": now(),
        "passed": gate_status.passed,
        "score": gate_status.score,
        "failures": [f.to_dict() for f in gate_status.failures],
        "resolution_time": None,  # Updated when resolved
        "team": context.team,
        "project": context.project
    }
    
    # Store in metrics database
    store_gate_metrics(metrics)
    
    # Update running statistics
    update_gate_statistics(gate_name, gate_status)
    
    # Detect trends
    detect_quality_trends(gate_name, context.team)
```

### 8. Integration with CI/CD

#### 8.1 Pre-Commit Hook
```bash
#!/bin/bash
# .git/hooks/pre-commit

echo "🔍 Running quality gate checks..."

# Execute pre-commit gate
bmad_gate_check pre_commit

if [ $? -ne 0 ]; then
    echo "❌ Quality gate failed. Fix issues before committing."
    echo "💡 Run 'bmad_gate_check pre_commit --guidance' for improvement suggestions"
    exit 1
fi

echo "✅ Quality gate passed"
```

#### 8.2 CI Pipeline Integration
```yaml
# .github/workflows/quality-gates.yml
quality_gates:
  pre_merge:
    runs-on: ubuntu-latest
    steps:
      - name: Run Quality Gate
        run: |
          bmad_gate_check pre_merge --strict
      
      - name: Generate Report
        if: failure()
        run: |
          bmad_gate_check report --format=markdown > gate-report.md
          
      - name: Comment on PR
        if: failure()
        uses: actions/comment@v1
        with:
          message-path: gate-report.md
```

### 9. Command Interface

#### 9.1 Gate Check Commands
```yaml
gate_commands:
  check:
    usage: "/gate-check [trigger] [--phase=<phase>]"
    description: "Run quality gate check for trigger point"
    examples:
      - "/gate-check pre_commit"
      - "/gate-check story_completion --phase=development"
      
  status:
    usage: "/gate-status [--detailed]"
    description: "Show current gate status and recent results"
    
  guidance:
    usage: "/gate-guidance [failure_id]"
    description: "Get improvement guidance for gate failure"
    
  override:
    usage: "/gate-override [gate] --reason='justification' --remedy-by=<date>"
    description: "Request gate override with justification"
    
  metrics:
    usage: "/gate-metrics [--team=<team>] [--period=<days>]"
    description: "View gate performance metrics"
```

This comprehensive quality gate check system ensures consistent quality enforcement through automation while providing helpful guidance for continuous improvement.