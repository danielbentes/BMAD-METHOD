# Quality Gate Configuration Reference

## Overview
Comprehensive configuration guide for all quality gates in the BMAD Method, including trigger points, enforcement levels, check definitions, and override policies.

## Gate Configuration Structure

```yaml
gate_configuration:
  metadata:
    version: "1.0"
    last_updated: "2024-01-06"
    total_gates: 15
    
  global_settings:
    automation_enabled: true
    memory_integration: true
    improvement_guidance: true
    metrics_tracking: true
    
  enforcement_policies:
    strict:
      description: "Zero tolerance - all checks must pass"
      override_allowed: false
      failure_action: "block_completely"
      notification: "immediate_team_wide"
      
    standard:
      description: "Critical checks must pass"
      override_allowed: true
      override_authority: "tech_lead_or_above"
      failure_action: "block_with_override_option"
      notification: "notify_responsible_parties"
      
    advisory:
      description: "Guidance only - no blocking"
      override_allowed: true
      override_authority: "any_team_member"
      failure_action: "warn_and_log"
      notification: "log_only"
```

## Phase-Based Gate Configurations

### Discovery Phase Gates

```yaml
discovery_gates:
  phase_entry:
    trigger: "phase_start"
    enforcement: "standard"
    automated_percentage: 100
    checks:
      - name: "context_restoration"
        type: "required"
        description: "Previous context loaded if available"
        implementation: "check_context_exists_and_load()"
        
      - name: "memory_initialization"
        type: "required"
        description: "Memory system ready"
        implementation: "verify_memory_connection()"
        
      - name: "workspace_setup"
        type: "required"
        description: "Project workspace configured"
        implementation: "validate_workspace_structure()"
        
  phase_exit:
    trigger: "phase_completion"
    enforcement: "standard"
    automated_percentage: 80
    checks:
      - name: "problem_definition_clarity"
        type: "threshold"
        threshold: 90
        measurement: "clarity_score"
        description: "Problem statement clearly defined"
        
      - name: "user_research_depth"
        type: "threshold"
        threshold: 85
        measurement: "research_completeness"
        description: "Target users researched and documented"
        
      - name: "scope_boundary_definition"
        type: "threshold"
        threshold: 95
        measurement: "scope_clarity_score"
        description: "Project boundaries clearly established"
        
      - name: "stakeholder_alignment"
        type: "manual"
        description: "Stakeholders aligned on vision"
        verification: "stakeholder_signoff_documented()"
```

### Requirements Phase Gates

```yaml
requirements_gates:
  phase_entry:
    trigger: "phase_start"
    enforcement: "strict"
    automated_percentage: 100
    checks:
      - name: "discovery_completion"
        type: "dependency"
        required_phase: "discovery"
        description: "Discovery phase successfully completed"
        
      - name: "pm_availability"
        type: "required"
        description: "Product Manager assigned and available"
        
      - name: "design_architect_availability"
        type: "required"
        description: "Design Architect assigned and available"
        
  phase_exit:
    trigger: "phase_completion"
    enforcement: "strict"
    automated_percentage: 85
    checks:
      - name: "prd_completeness"
        type: "threshold"
        threshold: 95
        measurement: "section_completion_percentage"
        description: "PRD has all required sections"
        sections:
          - executive_summary
          - user_stories
          - acceptance_criteria
          - technical_requirements
          - success_metrics
          
      - name: "acceptance_criteria_quality"
        type: "threshold"
        threshold: 100
        measurement: "stories_with_criteria_percentage"
        description: "All stories have clear acceptance criteria"
        
      - name: "ui_specification_completeness"
        type: "threshold"
        threshold: 90
        measurement: "ui_coverage_percentage"
        description: "UI flows and wireframes documented"
        
      - name: "technical_feasibility_validation"
        type: "threshold"
        threshold: 85
        measurement: "assumptions_validated_percentage"
        description: "Technical assumptions validated"
```

### Architecture Phase Gates

```yaml
architecture_gates:
  phase_entry:
    trigger: "phase_start"
    enforcement: "strict"
    automated_percentage: 100
    checks:
      - name: "requirements_approval"
        type: "dependency"
        required_phase: "requirements"
        description: "Requirements phase approved"
        
      - name: "architect_availability"
        type: "required"
        description: "Solution Architect assigned"
        
      - name: "udtm_readiness"
        type: "required"
        description: "Ready for Ultra-Deep Thinking Mode"
        
  phase_exit:
    trigger: "phase_completion"
    enforcement: "strict"
    automated_percentage: 75
    checks:
      - name: "architecture_analysis_tag"
        type: "required"
        description: "Architecture analysis tag present"
        tag_requirements:
          - current_state_analysis
          - proposed_architecture
          - trade_off_analysis
          - risk_assessment
          - decision_rationale
          
      - name: "scalability_design"
        type: "threshold"
        threshold: 90
        measurement: "scalability_score"
        description: "System designed for growth"
        criteria:
          - horizontal_scaling_capability
          - performance_under_load
          - resource_optimization
          
      - name: "security_architecture"
        type: "threshold"
        threshold: 95
        measurement: "security_coverage"
        description: "Security patterns implemented"
        requirements:
          - authentication_strategy
          - authorization_model
          - data_encryption
          - security_audit_logging
          
      - name: "performance_targets"
        type: "threshold"
        threshold: 85
        measurement: "performance_planning_score"
        description: "Performance targets defined"
        
      - name: "component_separation"
        type: "threshold"
        threshold: 95
        measurement: "modularity_score"
        description: "Clear component boundaries"
```

### Development Phase Gates

```yaml
development_gates:
  pre_commit:
    trigger: "code_staged"
    enforcement: "strict"
    automated_percentage: 100
    checks:
      - name: "linting"
        type: "threshold"
        threshold: 0
        measurement: "violation_count"
        description: "Zero linting errors"
        tools: ["ruff", "eslint", "pylint"]
        
      - name: "type_checking"
        type: "threshold"
        threshold: 0
        measurement: "type_error_count"
        description: "Zero type errors"
        tools: ["mypy", "typescript", "flow"]
        
      - name: "unit_tests"
        type: "threshold"
        threshold: 100
        measurement: "test_pass_rate"
        description: "All unit tests passing"
        
      - name: "style_consistency"
        type: "threshold"
        threshold: 95
        measurement: "style_compliance_score"
        description: "Code matches project patterns"
        
  story_completion:
    trigger: "story_done"
    enforcement: "strict"
    automated_percentage: 90
    checks:
      - name: "dod_checklist"
        type: "threshold"
        threshold: 100
        measurement: "checklist_completion"
        description: "Definition of Done complete"
        
      - name: "test_coverage"
        type: "threshold"
        threshold: 85
        measurement: "coverage_percentage"
        description: "Adequate test coverage"
        
      - name: "code_review_approval"
        type: "required"
        description: "Code review approved"
        minimum_reviewers: 1
        
      - name: "integration_tests"
        type: "threshold"
        threshold: 100
        measurement: "integration_test_pass_rate"
        description: "Integration tests passing"
        
      - name: "documentation_updated"
        type: "required"
        description: "Documentation reflects changes"
        
  sprint_end:
    trigger: "sprint_completion"
    enforcement: "standard"
    automated_percentage: 80
    checks:
      - name: "sprint_goal_achievement"
        type: "threshold"
        threshold: 90
        measurement: "goals_completed_percentage"
        description: "Sprint goals achieved"
        
      - name: "technical_debt_ratio"
        type: "threshold"
        threshold: 85
        measurement: "debt_health_score"
        description: "Technical debt controlled"
        
      - name: "performance_baseline"
        type: "threshold"
        threshold: 95
        measurement: "performance_maintenance"
        description: "Performance maintained"
        
      - name: "quality_metrics"
        type: "threshold"
        threshold: 90
        measurement: "overall_quality_score"
        description: "Quality standards maintained"
```

## Trigger-Based Gate Configurations

### Critical Change Gates

```yaml
critical_change_gates:
  architecture_modification:
    trigger: "architecture_file_changed"
    enforcement: "strict"
    automated_percentage: 95
    checks:
      - name: "impact_analysis"
        type: "required"
        description: "Impact analysis documented"
        
      - name: "backward_compatibility"
        type: "required"
        description: "Compatibility maintained"
        
      - name: "migration_plan"
        type: "required"
        description: "Migration strategy defined"
        
      - name: "architect_review"
        type: "required"
        description: "Architect approval obtained"
        
  security_component_change:
    trigger: "security_code_modified"
    enforcement: "strict"
    automated_percentage: 100
    override_allowed: false
    checks:
      - name: "security_scan"
        type: "required"
        description: "Security vulnerabilities scan"
        tools: ["snyk", "sonarqube", "dependabot"]
        
      - name: "penetration_test"
        type: "required"
        description: "Penetration testing passed"
        
      - name: "security_review"
        type: "required"
        description: "Security team approval"
        
      - name: "audit_logging"
        type: "required"
        description: "Changes logged for audit"
```

### Milestone Gates

```yaml
milestone_gates:
  25_percent_complete:
    trigger: "milestone_reached"
    enforcement: "standard"
    automated_percentage: 70
    checks:
      - name: "architecture_stability"
        type: "threshold"
        threshold: 90
        description: "Architecture decisions stable"
        
      - name: "requirement_stability"
        type: "threshold"
        threshold: 85
        description: "Requirements not changing"
        
      - name: "team_velocity"
        type: "threshold"
        threshold: 80
        description: "Team velocity on track"
        
  50_percent_complete:
    trigger: "milestone_reached"
    enforcement: "standard"
    automated_percentage: 75
    checks:
      - name: "feature_completion"
        type: "threshold"
        threshold: 45
        description: "Features on track"
        
      - name: "integration_stability"
        type: "threshold"
        threshold: 85
        description: "Integrations working"
        
      - name: "quality_trend"
        type: "threshold"
        threshold: 90
        description: "Quality improving"
        
  75_percent_complete:
    trigger: "milestone_reached"
    enforcement: "strict"
    automated_percentage: 85
    checks:
      - name: "feature_freeze"
        type: "required"
        description: "Feature development complete"
        
      - name: "bug_density"
        type: "threshold"
        threshold: 90
        description: "Bug count acceptable"
        
      - name: "performance_validation"
        type: "threshold"
        threshold: 95
        description: "Performance targets met"
        
  100_percent_complete:
    trigger: "milestone_reached"
    enforcement: "strict"
    automated_percentage: 95
    checks:
      - name: "all_features_complete"
        type: "threshold"
        threshold: 100
        description: "All features implemented"
        
      - name: "zero_critical_bugs"
        type: "threshold"
        threshold: 0
        measurement: "critical_bug_count"
        description: "No critical bugs"
        
      - name: "documentation_complete"
        type: "threshold"
        threshold: 100
        description: "Documentation finished"
        
      - name: "deployment_ready"
        type: "required"
        description: "Ready for production"
```

## Check Implementation Details

### Automated Check Types

```yaml
check_types:
  threshold:
    description: "Numeric comparison checks"
    implementation: |
      def evaluate_threshold(check, context):
          actual = measure_metric(check.metric, context)
          return compare_values(actual, check.threshold, check.operator)
    operators: [">=", "<=", "==", ">", "<"]
    
  required:
    description: "Binary presence checks"
    implementation: |
      def evaluate_required(check, context):
          return check_exists(check.target, context)
    
  pattern:
    description: "Pattern matching checks"
    implementation: |
      def evaluate_pattern(check, context):
          return match_pattern(check.pattern, context.content)
    
  dependency:
    description: "Prerequisite completion checks"
    implementation: |
      def evaluate_dependency(check, context):
          return is_complete(check.required_item, context)
```

### Manual Check Types

```yaml
manual_checks:
  review:
    description: "Human review required"
    process:
      - reviewer_assigned
      - review_completed
      - feedback_addressed
      - approval_granted
      
  stakeholder_approval:
    description: "Stakeholder sign-off"
    process:
      - presentation_scheduled
      - feedback_collected
      - concerns_addressed
      - approval_documented
      
  expert_validation:
    description: "Domain expert review"
    process:
      - expert_identified
      - review_requested
      - validation_complete
      - findings_documented
```

## Override Configuration

```yaml
override_configuration:
  authority_matrix:
    advisory_gates:
      required_role: "any_team_member"
      approval_process: "self_approval"
      documentation: "reason_only"
      
    standard_gates:
      required_role: "tech_lead"
      approval_process: "single_approval"
      documentation:
        - business_justification
        - remediation_timeline
        
    strict_gates:
      required_role: "architect_and_pm"
      approval_process: "dual_approval"
      documentation:
        - executive_justification
        - risk_assessment
        - mitigation_plan
        - accountability_assignment
        
    no_override_gates:
      - security_gates
      - data_integrity_gates
      - compliance_gates
      
  override_tracking:
    automatic_actions:
      - create_technical_debt_ticket
      - set_remediation_reminder
      - update_team_metrics
      - notify_stakeholders
      
    expiry_policy:
      default_expiry: "end_of_sprint"
      maximum_duration: "30_days"
      auto_escalate_expired: true
```

## Improvement Guidance Configuration

```yaml
improvement_guidance:
  memory_search_priorities:
    1: "exact_failure_match"
    2: "similar_failure_pattern"
    3: "team_success_history"
    4: "cross_team_solutions"
    5: "industry_best_practices"
    
  guidance_components:
    immediate_fix:
      time_limit: "30_minutes"
      complexity: "low"
      verification: "automated"
      
    proper_solution:
      time_limit: "4_hours"
      complexity: "medium"
      verification: "comprehensive"
      
    preventive_measure:
      implementation: "next_sprint"
      complexity: "varies"
      verification: "long_term_monitoring"
      
  success_tracking:
    metrics:
      - time_to_resolution
      - recurrence_rate
      - team_adoption
      - effectiveness_score
```

## Metrics and Reporting

```yaml
metrics_configuration:
  collection:
    frequency: "real_time"
    retention: "12_months"
    aggregation_levels:
      - individual
      - team
      - project
      - organization
      
  key_metrics:
    - gate_pass_rate
    - average_resolution_time
    - override_frequency
    - improvement_effectiveness
    - quality_trend
    - team_velocity_impact
    
  reporting:
    dashboards:
      - real_time_status
      - weekly_summary
      - monthly_trends
      - quarterly_analysis
      
    alerts:
      - gate_failure_spike
      - override_threshold_exceeded
      - quality_degradation
      - remediation_overdue
```

This comprehensive configuration ensures consistent quality gate enforcement while providing flexibility for different project phases and contexts.