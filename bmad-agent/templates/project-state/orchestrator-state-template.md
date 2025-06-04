# BMAD Orchestrator State (Memory-Enhanced)

```yaml
session_metadata:
  session_id: "{{SESSION_ID}}"
  created_timestamp: "{{CREATION_TIMESTAMP}}"
  last_updated: "{{LAST_UPDATED}}"
  bmad_version: v3.0
  user_id: "{{USER_ID}}"
  project_name: "{{PROJECT_NAME}}"
  project_type: "{{PROJECT_TYPE}}"  # brownfield|greenfield|mvp|feature
  session_duration: 0
  initialization_status: 'pending'
  initialization_timestamp: "{{CREATION_TIMESTAMP}}"
project_context_discovery:
  discovery_status:
    completed: false
    last_run: "{{CREATION_TIMESTAMP}}"
    confidence: 0
  project_analysis:
    domain: "{{PROJECT_DOMAIN}}"  # api|web-app|mobile|data-pipeline|etc
    technology_stack: []
    architecture_style: "{{ARCHITECTURE_STYLE}}"  # monolith|microservices|serverless
    team_size_inference: "{{TEAM_SIZE}}"  # 1-5|6-10|11+
    project_age: "{{PROJECT_AGE}}"  # new|established|legacy
    complexity_assessment: "{{COMPLEXITY}}"  # simple|moderate|complex|enterprise
  constraints:
    technical: []
    business: []
    timeline: reasonable
    budget: startup
active_workflow_context:
  current_state:
    active_persona: orchestrator
    current_phase: initialization
    workflow_type: "{{WORKFLOW_TYPE}}"  # new-project-mvp|feature-addition|refactoring|maintenance
    last_task: project-initialization
    task_status: in-progress
    next_suggested: project-analysis
  epic_context:
    current_epic: project-setup
    epic_status: in-progress
    epic_progress: 0
    story_context:
      current_story: bmad-initialization
      story_status: in-progress
      stories_completed: 0
      stories_remaining: 1
decision_archaeology:
  major_decisions: []
  pending_decisions: []
memory_intelligence_state:
  memory_provider: file-based-fallback
  memory_status: initializing
  openmemory_server_status: unknown
  openmemory_server_accessible: false
  mcp_tools_available: false
  last_memory_sync: "{{CREATION_TIMESTAMP}}"
  connection_metrics:
    server_latency_ms: 0.0
    server_accessible: false
    mcp_tool_availability: false
    total_connection_tests: 0
    last_check: "{{CREATION_TIMESTAMP}}"
  pattern_recognition:
    workflow_patterns: []
    decision_patterns: []
    anti_patterns_detected: []
    last_analysis: "{{CREATION_TIMESTAMP}}"
  user_preferences:
    communication_style: detailed
    workflow_style: systematic
    documentation_preference: comprehensive
    feedback_style: supportive
    confidence: 50
  proactive_intelligence:
    insights_generated: 0
    recommendations_active: 0
    warnings_issued: 0
    optimization_opportunities: 0
    last_update: "{{CREATION_TIMESTAMP}}"
    patterns_recognized: 0
  fallback_storage:
    total_memories: 0
    decisions: 0
    patterns: 0
    storage_file: .bmad/memory/fallback-storage.json
quality_framework_integration:
  quality_status:
    quality_gates_active: true
    current_gate: initialization
    gate_status: pending
  udtm_analysis:
    required_for_current_task: false
    last_completed: null
    completion_status: not-required
    confidence_achieved: 0
  brotherhood_reviews:
    pending_reviews: 0
    completed_reviews: 0
    review_effectiveness: 0
  anti_pattern_monitoring:
    scanning_active: true
    violations_detected: 0
    last_scan: "{{CREATION_TIMESTAMP}}"
    critical_violations: 0
system_health_monitoring:
  system_health:
    overall_status: initializing
    last_diagnostic: "{{CREATION_TIMESTAMP}}"
  configuration_health:
    config_file_status: valid
    config_last_loaded: "{{CREATION_TIMESTAMP}}"
    persona_files_status: all-present
    task_files_status: complete
  performance_metrics:
    average_response_time: 0
    memory_usage: 0
    cache_hit_rate: 0
    error_frequency: 0
    cpu_usage: 0
  resource_status:
    available_personas: 10
    personas_verified: true
    available_tasks: 22
    missing_resources: []
consultation_collaboration:
  consultation_history: []
  active_consultations: []
  collaboration_patterns:
    most_effective_pairs: []
    consultation_success_rate: 0
    average_resolution_time: 0
session_continuity_data:
  handoff_context:
    last_handoff_from: system
    last_handoff_to: orchestrator
    handoff_timestamp: "{{CREATION_TIMESTAMP}}"
    context_preserved: true
    handoff_effectiveness: 100
  workflow_intelligence:
    suggested_next_steps:
    - project-analysis
    - technology-stack-detection
    - team-context-setup
    predicted_blockers: []
    optimization_opportunities: []
    estimated_completion: "{{ESTIMATED_COMPLETION}}"
  session_variables:
    interaction_mode: standard
    verbosity_level: detailed
    auto_save_enabled: true
    memory_enhancement_active: true
    quality_enforcement_active: true
recent_activity_log:
  command_history: []
  insight_generation: []
  error_log_summary:
    recent_errors: 0
    critical_errors: 0
    last_error: null
    recovery_success_rate: 100
bootstrap_analysis_results:
  bootstrap_status:
    completed: false
    last_run: "{{CREATION_TIMESTAMP}}"
    analysis_confidence: 0
  project_archaeology:
    decisions_extracted: 0
    patterns_identified: 0
    preferences_inferred: 0
    technical_debt_assessed: false
  discovered_patterns:
    successful_approaches: []
    anti_patterns_found: []
    optimization_opportunities: []
    risk_factors: []
```

---
**Template Information**:
- **Template Version**: 1.0
- **Created**: {{CREATION_TIMESTAMP}}
- **For Project**: {{PROJECT_NAME}}
- **Initialization Status**: Template - requires project-specific initialization

**Next Steps After Copying**:
1. Replace all {{PLACEHOLDER}} values with project-specific data
2. Run project analysis and discovery
3. Initialize memory system for project context
4. Begin workflow with appropriate persona
