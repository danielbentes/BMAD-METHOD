# Memory Operations Task
<!-- Simplified task interface for memory operations -->
<!-- Full architecture: memory/memory-system-architecture.md -->

## CRITICAL SAFETY RULES - MANDATORY COMPLIANCE

### STOP CONDITIONS - ABORT IMMEDIATELY IF:
- Memory system shows data corruption indicators
- Sensitive data (passwords, API keys, PII) detected in memory content
- Memory operation would exceed system limits (>100MB)
- Circular reference detected in memory relationships
- User explicitly requests "no memory" or "forget this"

### MANDATORY VALIDATIONS BEFORE PROCEEDING:
1. **Memory System Health**: Verify memory service is operational
2. **Data Integrity**: Check for corruption in memory storage
3. **Privacy Scan**: Ensure no sensitive data in memory operations
4. **Size Limits**: Confirm operation within resource constraints
5. **User Consent**: Verify memory operations are authorized

### QUALITY GATES - MUST PASS ALL:
- [ ] Memory system accessible (or fallback available)
- [ ] No sensitive data detected in content
- [ ] Memory size within limits (<10KB per entry)
- [ ] Valid memory schema structure
- [ ] User consent confirmed or implied

> **Note**: This is the executable memory operations task. For detailed integration guidance and implementation details, see `bmad-agent/memory/memory-system-architecture.md`.

## Purpose
Execute memory-aware context management for the current session, integrating historical insights and patterns to enhance decision-making and maintain continuity across interactions. When memory system is unavailable, use fallback storage at `.bmad/system/memory/fallbacks/`.

## Progressive Disclosure Phases

### Phase 1: System Readiness (MANDATORY)
1. Check memory system availability
2. Verify data integrity
3. Scan for sensitive content
4. Confirm resource availability
5. **GATE**: System healthy → Continue to Phase 2

### Phase 2: Memory Query Optimization
1. Analyze current context
2. Build intelligent queries
3. Execute memory searches
4. Rank results by relevance
5. **GATE**: Relevant memories found → Continue to Phase 3

### Phase 3: Memory Integration
1. Synthesize memory insights
2. Apply to current context
3. Generate recommendations
4. Present enhanced guidance
5. **GATE**: Integration successful → Continue to Phase 4

### Phase 4: Memory Persistence
1. Capture new insights
2. Structure for storage
3. Validate before saving
4. Update memory indices
5. **FINAL GATE**: Memory updated → Task Complete

## Memory Categories & Schemas

### Decision Memories
**Schema**: `decision:{project}:{persona}:{timestamp}`
**Usage**: Track significant architectural, strategic, and tactical decisions with outcomes
**Content Structure**:
```json
{
  "type": "decision",
  "project": "project-name",
  "persona": "architect|pm|dev|etc",
  "decision": "chose-nextjs-over-react",
  "rationale": "better ssr support for seo requirements",
  "alternatives_considered": ["react+vite", "vue", "svelte"],
  "constraints": ["team-familiarity", "timeline", "seo-critical"],
  "outcome": "successful|problematic|unknown",
  "lessons": "nextjs learning curve was steeper than expected",
  "context_tags": ["frontend", "framework", "ssr", "seo"],
  "reusability_score": 0.8,
  "confidence_level": "high"
}
```

### Pattern Memories
**Schema**: `pattern:{workflow-type}:{success-indicator}`
**Usage**: Capture successful workflow patterns, sequences, and optimization insights
**Content Structure**:
```json
{
  "type": "workflow-pattern",
  "workflow": "new-project-mvp",
  "sequence": ["analyst", "pm", "architect", "design-architect", "po", "sm", "dev"],
  "decision_points": [
    {
      "stage": "pm-to-architect",
      "common_questions": ["monorepo vs polyrepo", "database choice"],
      "success_factors": ["clear-requirements", "defined-constraints"]
    }
  ],
  "success_indicators": {
    "time_to_first_code": "< 3 days",
    "architecture_stability": "no major changes after dev start",
    "user_satisfaction": "high"
  },
  "anti_patterns": ["skipping-po-validation", "architecture-without-prd"],
  "project_context": ["mvp", "startup", "web-app"],
  "effectiveness_score": 0.9
}
```

### Implementation Memories
**Schema**: `implementation:{technology}:{functionality}:{outcome}`
**Usage**: Track successful code patterns, debugging solutions, and technical approaches
**Content Structure**:
```json
{
  "type": "implementation",
  "technology_stack": ["nextjs", "typescript", "tailwind"],
  "functionality": "user-authentication",
  "approach": "jwt-with-refresh-tokens",
  "code_patterns": ["custom-hook-useAuth", "context-provider-pattern"],
  "challenges": ["token-refresh-timing", "secure-storage"],
  "solutions": ["axios-interceptor", "httponly-cookies"],
  "performance_impact": "minimal",
  "security_considerations": ["csrf-protection", "xss-prevention"],
  "testing_approach": ["unit-tests-auth-hook", "integration-tests-login-flow"],
  "maintenance_notes": "token expiry config needs environment-specific tuning",
  "success_metrics": {
    "implementation_time": "2 days",
    "bug_count": 0,
    "performance_score": 95
  }
}
```

### Consultation Memories
**Schema**: `consultation:{type}:{participants}:{outcome}`
**Usage**: Capture multi-persona consultation outcomes and collaborative insights
**Content Structure**:
```json
{
  "type": "consultation",
  "consultation_type": "design-review",
  "participants": ["pm", "architect", "design-architect"],
  "problem": "database scaling for real-time features",
  "perspectives": {
    "pm": "user-experience priority, cost concerns",
    "architect": "technical feasibility, performance requirements", 
    "design-architect": "ui responsiveness, loading states"
  },
  "consensus": "implement caching layer with websockets",
  "minority_opinions": ["architect preferred event-sourcing approach"],
  "implementation_success": true,
  "follow_up_needed": false,
  "reusable_insights": ["caching-before-scaling", "websocket-ui-patterns"],
  "collaboration_effectiveness": 0.9,
  "decision_confidence": 0.8
}
```

### User Preference Memories
**Schema**: `preference:{user-context}:{preference-type}`
**Usage**: Learn individual working styles, preferences, and successful interaction patterns
**Content Structure**:
```json
{
  "type": "user-preference",
  "preference_category": "workflow-style",
  "preference": "detailed-technical-explanations",
  "context": "architecture-discussions",
  "evidence": ["requested-deep-dives", "positive-feedback-on-technical-detail"],
  "confidence": 0.7,
  "patterns": ["prefers-incremental-approach", "values-cross-references"],
  "adaptations": ["provide-more-technical-context", "include-implementation-examples"],
  "effectiveness": "high"
}
```

## Memory Operations Integration

### Intelligent Memory Queries
**Query Strategy Framework**:
```python
def build_contextual_memory_queries(current_context):
    queries = []
    
    # Direct relevance search
    if current_context.persona and current_context.task:
        queries.append(f"decisions involving {current_context.persona} and {extract_key_terms(current_context.task)}")
    
    # Pattern matching search  
    if current_context.project_phase and current_context.tech_stack:
        queries.append(f"successful patterns for {current_context.project_phase} with {current_context.tech_stack}")
    
    # Problem similarity search
    if current_context.blockers:
        queries.append(f"solutions for {current_context.blockers}")
    
    # Anti-pattern prevention
    queries.append(f"mistakes to avoid when {current_context.task} with {current_context.persona}")
    
    # Implementation guidance
    if current_context.implementation_context:
        queries.append(f"successful implementation {current_context.implementation_context}")
    
    return queries

def search_memory_with_context(queries, threshold=0.7):
    relevant_memories = []
    for query in queries:
        memories = search_memory(query, limit=3, threshold=threshold)
        relevant_memories.extend(memories)
    
    # Deduplicate and rank by relevance
    return deduplicate_and_rank(relevant_memories)
```

### Memory Integration Patterns by Operation Type

#### Decision Operations
**Pattern**: Context-Aware Decision Enhancement
```python
def enhance_decision_with_memory(decision_context):
    """Enhance decision-making with historical insights"""
    # 1. Search for similar past decisions
    similar_decisions = search_memory(
        f"decision {decision_context.domain} {decision_context.constraints}",
        filter_tags=["decision", decision_context.persona]
    )
    
    # 2. Extract outcome patterns
    successful_patterns = filter(lambda d: d.outcome == "successful", similar_decisions)
    failed_patterns = filter(lambda d: d.outcome == "problematic", similar_decisions)
    
    # 3. Generate proactive warnings
    warnings = []
    for failure in failed_patterns:
        if similarity(failure.context, decision_context) > 0.8:
            warnings.append({
                "risk": failure.lessons,
                "mitigation": failure.recovery_approach,
                "confidence": failure.pattern_strength
            })
    
    # 4. Surface best practices
    recommendations = []
    for success in successful_patterns:
        recommendations.append({
            "approach": success.decision_path,
            "rationale": success.key_factors,
            "expected_outcome": success.results,
            "confidence": calculate_confidence(success, decision_context)
        })
    
    return {
        "historical_context": similar_decisions,
        "warnings": warnings,
        "recommendations": sorted(recommendations, key=lambda r: r["confidence"], reverse=True)[:3],
        "decision_confidence": calculate_overall_confidence(similar_decisions, decision_context)
    }
```

#### Implementation Operations
**Pattern**: Code Pattern Recognition & Reuse
```python
def enhance_implementation_with_patterns(implementation_context):
    """Apply successful implementation patterns"""
    # 1. Find similar implementations
    code_patterns = search_memory(
        f"implementation {implementation_context.functionality} {implementation_context.tech_stack}",
        filter_tags=["implementation", "success"]
    )
    
    # 2. Pattern recognition and adaptation
    applicable_patterns = []
    for pattern in code_patterns:
        if is_pattern_applicable(pattern, implementation_context):
            adapted_pattern = adapt_pattern_to_context(pattern, implementation_context)
            applicable_patterns.append({
                "pattern": adapted_pattern,
                "success_rate": pattern.success_metrics.bug_count == 0,
                "performance_score": pattern.success_metrics.performance_score,
                "adaptation_notes": generate_adaptation_guide(pattern, implementation_context)
            })
    
    # 3. Test strategy inference
    test_strategies = extract_test_patterns(code_patterns, implementation_context)
    
    # 4. Performance optimization hints
    optimization_hints = extract_optimization_patterns(code_patterns)
    
    return {
        "code_patterns": sorted(applicable_patterns, key=lambda p: p["success_rate"], reverse=True),
        "test_strategies": test_strategies,
        "optimization_hints": optimization_hints,
        "common_pitfalls": extract_pitfalls(code_patterns)
    }
```

#### Workflow Operations
**Pattern**: Workflow Optimization Through Pattern Analysis
```python
def optimize_workflow_with_memory(workflow_context):
    """Optimize workflows based on historical patterns"""
    # 1. Retrieve similar workflow patterns
    workflow_patterns = search_memory(
        f"workflow {workflow_context.type} {workflow_context.constraints}",
        filter_tags=["workflow-pattern", "effective"]
    )
    
    # 2. Analyze sequence effectiveness
    sequence_analysis = analyze_persona_sequences(workflow_patterns, workflow_context)
    
    # 3. Identify optimization opportunities
    optimizations = []
    for pattern in workflow_patterns:
        if pattern.effectiveness_score > 0.8:
            optimization = {
                "step_to_optimize": identify_bottleneck(pattern, workflow_context),
                "optimization_approach": pattern.optimization_technique,
                "expected_improvement": pattern.time_saved,
                "risk_level": assess_optimization_risk(pattern, workflow_context)
            }
            optimizations.append(optimization)
    
    # 4. Cross-functional insights
    cross_functional = extract_collaboration_patterns(workflow_patterns)
    
    return {
        "optimal_sequence": sequence_analysis.best_sequence,
        "optimization_opportunities": sorted(optimizations, key=lambda o: o["expected_improvement"], reverse=True),
        "collaboration_insights": cross_functional,
        "success_predictors": extract_success_factors(workflow_patterns)
    }
```

#### Consultation Operations
**Pattern**: Multi-Perspective Synthesis Enhancement
```python
def enhance_consultation_with_memory(consultation_context):
    """Enhance multi-persona consultations with historical insights"""
    # 1. Find similar consultations
    past_consultations = search_memory(
        f"consultation {consultation_context.type} {consultation_context.problem_domain}",
        filter_tags=["consultation", consultation_context.type]
    )
    
    # 2. Extract consensus patterns
    consensus_patterns = analyze_consensus_formation(past_consultations)
    
    # 3. Predict potential conflicts
    conflict_predictions = []
    for consultation in past_consultations:
        if has_similar_participants(consultation, consultation_context):
            conflicts = extract_conflict_patterns(consultation)
            conflict_predictions.extend([{
                "potential_conflict": conflict,
                "resolution_approach": consultation.resolution_strategy,
                "prevention_tactic": generate_prevention_strategy(conflict, consultation_context)
            }])
    
    # 4. Success factor analysis
    success_factors = extract_consultation_success_factors(past_consultations)
    
    return {
        "consensus_strategies": consensus_patterns,
        "conflict_predictions": conflict_predictions,
        "success_factors": success_factors,
        "facilitation_tips": generate_facilitation_guide(past_consultations, consultation_context),
        "expected_duration": estimate_consultation_duration(past_consultations, consultation_context)
    }
```

### Proactive Memory Surfacing
**Intelligence Categories**:
1. **Immediate Relevance**: Direct matches to current context
2. **Pattern Recognition**: Similar situations with successful outcomes
3. **Anti-Pattern Prevention**: Common mistakes in similar contexts
4. **Optimization Opportunities**: Performance/quality improvements from similar projects
5. **User Personalization**: Preferences and effective interaction patterns

#### Proactive Intelligence Hooks
```python
class ProactiveMemoryIntelligence:
    """Proactive memory surfacing based on context triggers"""
    
    def __init__(self, memory_system, context_monitor):
        self.memory = memory_system
        self.monitor = context_monitor
        self.intelligence_hooks = self._register_hooks()
    
    def _register_hooks(self):
        """Register context triggers for proactive memory surfacing"""
        return {
            "task_start": self.on_task_start,
            "decision_point": self.on_decision_point,
            "error_detected": self.on_error_detected,
            "pattern_match": self.on_pattern_match,
            "consultation_request": self.on_consultation_request,
            "handoff_initiated": self.on_handoff_initiated,
            "quality_gate": self.on_quality_gate,
            "user_question": self.on_user_question
        }
    
    def on_task_start(self, task_context):
        """Surface relevant memories when starting a new task"""
        memories = {
            "similar_tasks": self.memory.search(
                f"task {task_context.type} {task_context.domain}",
                filter_success=True
            ),
            "common_blockers": self.memory.search(
                f"blockers {task_context.type}",
                filter_tags=["lesson-learned"]
            ),
            "best_practices": self.memory.search(
                f"best practice {task_context.type}",
                min_confidence=0.8
            ),
            "time_estimates": self._estimate_task_duration(task_context)
        }
        
        return self._format_proactive_insights(memories, "task_start")
    
    def on_decision_point(self, decision_context):
        """Provide insights when a decision is needed"""
        # Analyze decision patterns
        similar_decisions = self.memory.search(
            f"decision {decision_context.domain} {decision_context.constraints}"
        )
        
        # Group by outcome
        outcomes = self._analyze_decision_outcomes(similar_decisions)
        
        # Generate recommendations
        insights = {
            "historical_outcomes": outcomes,
            "success_factors": self._extract_success_factors(similar_decisions),
            "risk_factors": self._extract_risk_factors(similar_decisions),
            "recommended_approach": self._recommend_decision_path(outcomes, decision_context),
            "confidence_level": self._calculate_recommendation_confidence(similar_decisions)
        }
        
        return self._format_proactive_insights(insights, "decision_support")
    
    def on_error_detected(self, error_context):
        """Provide immediate help when errors occur"""
        # Search for similar errors
        similar_errors = self.memory.search(
            f"error {error_context.type} {error_context.technology}",
            include_solutions=True
        )
        
        # Prioritize by solution effectiveness
        solutions = []
        for error_memory in similar_errors:
            if error_memory.solution_effectiveness > 0.7:
                solutions.append({
                    "solution": error_memory.solution,
                    "context": error_memory.context,
                    "effectiveness": error_memory.solution_effectiveness,
                    "implementation_time": error_memory.fix_duration
                })
        
        insights = {
            "immediate_solutions": sorted(solutions, key=lambda s: s["effectiveness"], reverse=True)[:3],
            "root_causes": self._analyze_root_causes(similar_errors),
            "prevention_strategies": self._extract_prevention_strategies(similar_errors)
        }
        
        return self._format_proactive_insights(insights, "error_recovery", priority="high")
    
    def on_pattern_match(self, pattern_context):
        """Alert when significant patterns are detected"""
        if pattern_context.pattern_type == "anti-pattern":
            # Urgent intervention for anti-patterns
            interventions = self.memory.search(
                f"anti-pattern intervention {pattern_context.pattern_name}",
                urgency="high"
            )
            
            return {
                "alert_level": "high",
                "pattern_detected": pattern_context.pattern_name,
                "immediate_actions": self._extract_interventions(interventions),
                "consequences_if_continued": self._predict_consequences(pattern_context)
            }
        
        elif pattern_context.pattern_type == "success-pattern":
            # Reinforce positive patterns
            reinforcements = self.memory.search(
                f"success pattern reinforcement {pattern_context.pattern_name}"
            )
            
            return {
                "alert_level": "info",
                "pattern_detected": pattern_context.pattern_name,
                "optimization_opportunities": self._extract_optimizations(reinforcements),
                "expected_benefits": self._calculate_pattern_benefits(pattern_context)
            }
    
    def _estimate_task_duration(self, task_context):
        """Estimate task duration based on historical data"""
        similar_tasks = self.memory.search(
            f"task duration {task_context.type} {task_context.complexity}"
        )
        
        if not similar_tasks:
            return {"estimate": "unknown", "confidence": 0}
        
        durations = [task.actual_duration for task in similar_tasks]
        return {
            "estimate": statistics.median(durations),
            "range": (min(durations), max(durations)),
            "confidence": len(durations) / 10,  # More data = higher confidence
            "factors": self._extract_duration_factors(similar_tasks)
        }
    
    def _format_proactive_insights(self, insights, trigger_type, priority="normal"):
        """Format insights for presentation"""
        return {
            "trigger": trigger_type,
            "priority": priority,
            "timestamp": datetime.utcnow().isoformat(),
            "insights": insights,
            "presentation": self._generate_presentation(insights, trigger_type)
        }
```

### Memory Creation Automation
**Auto-Memory Triggers**:
```python
def auto_create_memory(event_type, content, context):
    memory_triggers = {
        "major_decision": lambda: create_decision_memory(content, context),
        "workflow_completion": lambda: create_pattern_memory(content, context),
        "successful_implementation": lambda: create_implementation_memory(content, context),
        "consultation_outcome": lambda: create_consultation_memory(content, context),
        "user_preference_signal": lambda: create_preference_memory(content, context),
        "problem_resolution": lambda: create_solution_memory(content, context),
        "lesson_learned": lambda: create_learning_memory(content, context)
    }
    
    if event_type in memory_triggers:
        memory_triggers[event_type]()
        
def create_contextual_memory_tags(content, context):
    tags = []
    
    # Automatic tagging based on content analysis
    tags.extend(extract_tech_terms(content))
    tags.extend(extract_domain_concepts(content))
    
    # Context-based tagging
    tags.append(f"phase:{context.phase}")
    tags.append(f"persona:{context.active_persona}")
    tags.append(f"project-type:{context.project_type}")
    
    # Semantic tagging for searchability
    tags.extend(generate_semantic_tags(content))
    
    return tags
```

### Pattern Recognition Integration
```python
class MemoryPatternRecognizer:
    """Advanced pattern recognition across memory entries"""
    
    def __init__(self, memory_system):
        self.memory = memory_system
        self.pattern_cache = {}
        self.recognition_threshold = 0.75
    
    def recognize_patterns(self, context):
        """Identify patterns relevant to current context"""
        patterns = {
            "workflow_patterns": self._find_workflow_patterns(context),
            "decision_patterns": self._find_decision_patterns(context),
            "error_patterns": self._find_error_patterns(context),
            "success_patterns": self._find_success_patterns(context),
            "collaboration_patterns": self._find_collaboration_patterns(context),
            "optimization_patterns": self._find_optimization_patterns(context)
        }
        
        # Cross-reference patterns for deeper insights
        cross_patterns = self._cross_reference_patterns(patterns)
        
        return {
            "identified_patterns": patterns,
            "cross_references": cross_patterns,
            "recommendations": self._generate_pattern_recommendations(patterns, context),
            "confidence_scores": self._calculate_pattern_confidence(patterns)
        }
    
    def _find_workflow_patterns(self, context):
        """Identify recurring workflow sequences"""
        workflow_memories = self.memory.search(
            f"workflow {context.project_type}",
            filter_tags=["workflow-pattern"]
        )
        
        # Sequence analysis
        sequences = {}
        for memory in workflow_memories:
            sequence_key = "->".join(memory.sequence)
            if sequence_key not in sequences:
                sequences[sequence_key] = {
                    "count": 0,
                    "success_rate": 0,
                    "avg_duration": 0,
                    "contexts": []
                }
            
            sequences[sequence_key]["count"] += 1
            sequences[sequence_key]["success_rate"] += memory.success_indicators.get("effectiveness", 0)
            sequences[sequence_key]["contexts"].append(memory.project_context)
        
        # Identify dominant patterns
        dominant_patterns = []
        for seq, data in sequences.items():
            if data["count"] >= 3:  # Minimum occurrences for pattern
                data["success_rate"] /= data["count"]
                if data["success_rate"] > self.recognition_threshold:
                    dominant_patterns.append({
                        "sequence": seq,
                        "strength": data["count"] / len(workflow_memories),
                        "success_rate": data["success_rate"],
                        "applicable_contexts": self._analyze_contexts(data["contexts"])
                    })
        
        return sorted(dominant_patterns, key=lambda p: p["strength"], reverse=True)
    
    def _find_decision_patterns(self, context):
        """Identify decision-making patterns"""
        decision_memories = self.memory.search(
            f"decision {context.domain}",
            filter_tags=["decision"]
        )
        
        # Group by decision type and outcome
        decision_groups = {}
        for memory in decision_memories:
            key = f"{memory.decision_type}:{memory.outcome}"
            if key not in decision_groups:
                decision_groups[key] = []
            decision_groups[key].append(memory)
        
        # Extract patterns
        patterns = []
        for group_key, memories in decision_groups.items():
            if len(memories) >= 2:  # Minimum for pattern
                common_factors = self._extract_common_factors(memories)
                if common_factors["similarity"] > self.recognition_threshold:
                    patterns.append({
                        "decision_type": group_key.split(":")[0],
                        "typical_outcome": group_key.split(":")[1],
                        "common_factors": common_factors["factors"],
                        "confidence": common_factors["similarity"],
                        "sample_size": len(memories)
                    })
        
        return patterns
    
    def _find_error_patterns(self, context):
        """Identify recurring error patterns and their solutions"""
        error_memories = self.memory.search(
            f"error {context.technology}",
            filter_tags=["error", "bug", "issue"]
        )
        
        # Cluster similar errors
        error_clusters = self._cluster_errors(error_memories)
        
        patterns = []
        for cluster in error_clusters:
            if len(cluster) >= 2:
                pattern = {
                    "error_type": self._identify_error_type(cluster),
                    "common_causes": self._extract_common_causes(cluster),
                    "effective_solutions": self._rank_solutions(cluster),
                    "prevention_strategies": self._derive_prevention_strategies(cluster),
                    "occurrence_rate": len(cluster) / len(error_memories),
                    "avg_fix_time": self._calculate_avg_fix_time(cluster)
                }
                patterns.append(pattern)
        
        return patterns
    
    def _cross_reference_patterns(self, patterns):
        """Find relationships between different pattern types"""
        cross_refs = []
        
        # Workflow -> Error correlations
        for workflow in patterns.get("workflow_patterns", []):
            for error in patterns.get("error_patterns", []):
                correlation = self._calculate_correlation(workflow, error)
                if correlation > 0.6:
                    cross_refs.append({
                        "type": "workflow_error_correlation",
                        "workflow": workflow["sequence"],
                        "error": error["error_type"],
                        "correlation": correlation,
                        "insight": f"This workflow sequence often leads to {error['error_type']} errors"
                    })
        
        # Decision -> Success correlations
        for decision in patterns.get("decision_patterns", []):
            for success in patterns.get("success_patterns", []):
                correlation = self._calculate_correlation(decision, success)
                if correlation > 0.7:
                    cross_refs.append({
                        "type": "decision_success_correlation",
                        "decision_factors": decision["common_factors"],
                        "success_indicators": success["indicators"],
                        "correlation": correlation,
                        "insight": "These decision factors strongly predict success"
                    })
        
        return cross_refs
    
    def _generate_pattern_recommendations(self, patterns, context):
        """Generate actionable recommendations from patterns"""
        recommendations = []
        
        # Workflow recommendations
        if patterns.get("workflow_patterns"):
            best_workflow = patterns["workflow_patterns"][0]  # Highest strength
            recommendations.append({
                "category": "workflow",
                "recommendation": f"Use workflow sequence: {best_workflow['sequence']}",
                "rationale": f"Success rate: {best_workflow['success_rate']:.1%} in similar contexts",
                "confidence": best_workflow["strength"]
            })
        
        # Error prevention recommendations
        if patterns.get("error_patterns"):
            for error_pattern in patterns["error_patterns"][:3]:  # Top 3 risks
                recommendations.append({
                    "category": "risk_prevention",
                    "recommendation": f"Implement prevention for {error_pattern['error_type']}",
                    "rationale": f"Occurs in {error_pattern['occurrence_rate']:.1%} of similar projects",
                    "prevention_steps": error_pattern["prevention_strategies"],
                    "confidence": 0.8
                })
        
        # Optimization recommendations
        if patterns.get("optimization_patterns"):
            for opt_pattern in patterns["optimization_patterns"]:
                if opt_pattern["improvement_potential"] > 0.2:  # 20% improvement threshold
                    recommendations.append({
                        "category": "optimization",
                        "recommendation": opt_pattern["optimization_approach"],
                        "expected_improvement": f"{opt_pattern['improvement_potential']:.1%}",
                        "implementation_effort": opt_pattern["effort_level"],
                        "confidence": opt_pattern["validation_strength"]
                    })
        
        return sorted(recommendations, key=lambda r: r.get("confidence", 0), reverse=True)
```

### Cross-Session Continuity Mechanisms
```python
class SessionContinuityManager:
    """Maintain continuity across sessions with memory integration"""
    
    def __init__(self, memory_system, session_storage):
        self.memory = memory_system
        self.session = session_storage
        self.continuity_threshold = 0.7
    
    def restore_session_context(self, user_id, project_id):
        """Restore context from previous sessions"""
        # 1. Load last session state
        last_session = self.session.get_last_session(user_id, project_id)
        
        # 2. Retrieve session memories
        session_memories = self.memory.search(
            f"session {user_id} {project_id}",
            time_range=last_session.get("timestamp", None),
            limit=20
        )
        
        # 3. Build continuity context
        continuity_context = {
            "last_active": last_session.get("timestamp"),
            "last_persona": last_session.get("active_persona"),
            "last_task": last_session.get("current_task"),
            "pending_items": self._extract_pending_items(last_session, session_memories),
            "decisions_made": self._summarize_decisions(session_memories),
            "current_blockers": self._identify_blockers(session_memories),
            "progress_summary": self._generate_progress_summary(session_memories),
            "next_steps": self._suggest_next_steps(last_session, session_memories)
        }
        
        # 4. Apply user preferences
        user_preferences = self._get_user_preferences(user_id)
        continuity_context = self._apply_preferences(continuity_context, user_preferences)
        
        return continuity_context
    
    def bridge_session_gap(self, time_gap, last_context, current_context):
        """Bridge gaps between sessions intelligently"""
        if time_gap.days > 7:
            # Long gap - provide comprehensive recap
            return self._generate_comprehensive_recap(last_context, current_context)
        elif time_gap.days > 1:
            # Medium gap - provide focused summary
            return self._generate_focused_summary(last_context, current_context)
        else:
            # Short gap - provide quick context
            return self._generate_quick_context(last_context, current_context)
    
    def maintain_project_momentum(self, project_context):
        """Keep project momentum across sessions"""
        momentum_data = {
            "velocity_trend": self._calculate_velocity_trend(project_context),
            "blocking_issues": self._identify_momentum_blockers(project_context),
            "upcoming_milestones": self._extract_milestones(project_context),
            "team_sentiment": self._analyze_team_sentiment(project_context),
            "risk_indicators": self._assess_project_risks(project_context)
        }
        
        # Generate momentum insights
        insights = []
        
        if momentum_data["velocity_trend"]["direction"] == "decreasing":
            insights.append({
                "type": "velocity_warning",
                "message": "Project velocity has decreased by {:.1%}".format(
                    momentum_data["velocity_trend"]["change"]
                ),
                "recommendations": self._generate_velocity_recommendations(momentum_data)
            })
        
        if momentum_data["blocking_issues"]:
            insights.append({
                "type": "blocker_alert",
                "blockers": momentum_data["blocking_issues"],
                "resolution_strategies": self._suggest_blocker_resolutions(momentum_data["blocking_issues"])
            })
        
        return {
            "momentum_status": momentum_data,
            "insights": insights,
            "recommended_actions": self._prioritize_momentum_actions(momentum_data)
        }
    
    def _extract_pending_items(self, last_session, memories):
        """Extract incomplete items from previous sessions"""
        pending = []
        
        # From last session state
        if last_session.get("pending_tasks"):
            pending.extend(last_session["pending_tasks"])
        
        # From memory analysis
        for memory in memories:
            if memory.get("status") == "in_progress" or memory.get("completion") < 1.0:
                pending.append({
                    "item": memory.get("description"),
                    "type": memory.get("type"),
                    "priority": memory.get("priority", "medium"),
                    "age": self._calculate_item_age(memory.get("created_at")),
                    "context": memory.get("context")
                })
        
        # Deduplicate and prioritize
        return self._prioritize_pending_items(pending)
    
    def _suggest_next_steps(self, last_session, memories):
        """Suggest next steps based on session history"""
        suggestions = []
        
        # Analyze patterns in session progression
        progression_pattern = self._analyze_progression_pattern(memories)
        
        # Based on last activity
        if last_session.get("last_activity_type") == "planning":
            suggestions.append({
                "action": "Begin implementation",
                "rationale": "Planning phase appears complete",
                "confidence": 0.8
            })
        elif last_session.get("last_activity_type") == "debugging":
            suggestions.append({
                "action": "Verify fix and add tests",
                "rationale": "Debugging session needs validation",
                "confidence": 0.9
            })
        
        # Based on patterns
        if progression_pattern.get("next_likely_step"):
            suggestions.append({
                "action": progression_pattern["next_likely_step"],
                "rationale": f"Based on {progression_pattern['pattern_strength']} similar progressions",
                "confidence": progression_pattern["confidence"]
            })
        
        return sorted(suggestions, key=lambda s: s["confidence"], reverse=True)
```

## Context Restoration with Memory Enhancement

### Multi-Layer Context Assembly Process

#### Layer 1 - Immediate Session Context
```markdown
# 📍 Current Session State
**Project Phase**: {current_phase}
**Active Persona**: {current_persona} 
**Last Activity**: {last_completed_task}
**Pending Items**: {current_blockers_and_concerns}
**Session Duration**: {active_time}
```

#### Layer 2 - Historical Memory Context
```markdown
# 📚 Relevant Historical Context
**Similar Situations**: {count} relevant memories found
**Success Patterns**: 
- {pattern_1}: Used in {project_name} with {success_rate}% success
- {pattern_2}: Applied {usage_count} times with {outcome_summary}

**Lessons Learned**:
- ✅ **What worked**: {successful_approaches}
- ⚠️ **What to avoid**: {anti_patterns_and_pitfalls}
- 🔧 **Best practices**: {proven_optimization_approaches}
```

#### Layer 3 - Proactive Intelligence
```markdown
# 💡 Proactive Insights
**Optimization Opportunities**: {performance_improvements_based_on_similar_contexts}
**Risk Prevention**: {common_issues_to_watch_for}
**Personalized Recommendations**: {user_preference_based_suggestions}
**Cross-Project Learning**: {insights_from_similar_projects}
```

### Context Synthesis & Presentation
**Intelligent Summary Generation**:
```markdown
# 🧠 Memory-Enhanced Context for {Target Persona}

## Current Situation
**Project**: {project_name} | **Phase**: {current_phase}
**Last Activity**: {last_persona} completed {last_task}
**Context**: {brief_situation_summary}

## 🎯 Directly Relevant Memory Insights
{synthesized_relevant_context_from_memories}

## 📈 Success Pattern Application
**Recommended Approach**: {best_practice_pattern}
**Based On**: {similar_successful_contexts}
**Confidence**: {confidence_score}% (from {evidence_count} similar cases)

## ⚠️ Proactive Warnings
**Potential Issues**: {common_pitfalls_for_context}
**Prevention Strategy**: {proven_avoidance_approaches}

## 🚀 Optimization Opportunities
**Performance**: {performance_improvement_suggestions}
**Efficiency**: {workflow_optimization_opportunities}
**Quality**: {quality_enhancement_recommendations}

## ❓ Contextual Questions
Based on memory patterns, consider:
1. {contextual_question_1}
2. {contextual_question_2}

---
💬 **Memory Query**: Ask "What do you remember about..." or "Show me patterns for..."
```

## Memory System Integration Instructions

### Safe Memory Operations Protocol

#### Pre-Operation Validation:
```python
def validate_memory_operation(content, operation_type):
    """Validate memory operation before execution"""
    validations = {
        "size_check": len(content) < 10240,  # 10KB limit
        "sensitive_data": not contains_sensitive_data(content),
        "schema_valid": validate_memory_schema(content),
        "no_corruption": check_data_integrity(content),
        "user_consent": has_memory_consent()
    }
    
    if not all(validations.values()):
        failed = [k for k, v in validations.items() if not v]
        raise MemoryValidationError(f"Failed validations: {failed}")
    
    return True
```

#### OpenMemory MCP Integration:
```python
# Memory function usage patterns with safety
def integrate_memory_with_bmad_operations():
    try:
        # Validate before storing
        content = "decision: chose postgresql for primary database"
        validate_memory_operation(content, "store")
        
        # Store significant events
        add_memories(
            content=sanitize_content(content),
            tags=["database", "architecture", "postgresql"],
            metadata={
                "project": current_project,
                "persona": "architect", 
                "confidence": 0.9,
                "reusability": 0.8,
                "timestamp": utc_now(),
                "validation_passed": True
            }
        )
        
        # Retrieve with safety limits
        relevant_context = search_memory(
            sanitize_query("database choice postgresql architecture decision"),
            limit=5,
            threshold=0.7,
            timeout=5000  # 5 second timeout
        )
        
        # Browse with filtering
        all_architecture_memories = list_memories(
            filter_tags=["architecture", "database"],
            limit=10,
            exclude_sensitive=True
        )
        
    except MemoryValidationError as e:
        log_validation_failure(e)
        use_fallback_storage()
    except MemoryTimeoutError:
        log_timeout()
        return cached_memories()
```

### Error Handling & Fallback:

#### Comprehensive Error Recovery:
```python
def memory_enhanced_operation_with_fallback():
    """Execute memory operation with multiple fallback levels"""
    error_count = 0
    max_retries = 3
    
    while error_count < max_retries:
        try:
            # Primary: Use memory system
            validate_memory_availability()
            memory_context = search_memory(
                sanitize_query(current_context_query),
                timeout=5000
            )
            validate_memory_response(memory_context)
            return enhanced_operation_with_memory(memory_context)
            
        except MemoryUnavailableError:
            # Secondary: Use fallback storage
            log_memory_unavailable()
            fallback_context = load_fallback_memories(
                ".bmad/system/memory/fallbacks/",
                validate=True
            )
            if fallback_context:
                return enhanced_operation_with_fallback(fallback_context)
            error_count += 1
            
        except MemoryCorruptionError as e:
            # Critical: Data corruption detected
            log_critical_error(e)
            quarantine_corrupted_memory(e.memory_id)
            notify_user("Memory corruption detected, using safe mode")
            return safe_mode_operation()
            
        except MemoryTimeoutError:
            # Performance: Timeout occurred
            log_timeout()
            if error_count == 0:
                # Try with reduced scope
                current_context_query = simplify_query(current_context_query)
            error_count += 1
            
        except Exception as e:
            # Unknown error
            log_memory_error(e)
            save_to_fallback(
                ".bmad/system/memory/fallbacks/error-recovery.md",
                sanitize_content(current_context)
            )
            error_count += 1
    
    # All retries exhausted
    return fallback_operation()

def save_to_fallback(path, content):
    """Save memory content to fallback file storage with validation"""
    try:
        # Validate content before saving
        if contains_sensitive_data(content):
            content = redact_sensitive_data(content)
        
        # Ensure directory exists
        ensure_directory_exists(".bmad/system/memory/fallbacks/")
        
        # Check disk space
        if not has_sufficient_space(len(content)):
            cleanup_old_fallbacks()
        
        # Write with atomic operation
        temp_path = f"{path}.tmp"
        with open(temp_path, 'w') as f:
            f.write(f"\n## {timestamp()}\n")
            f.write(f"### Safety Check: Passed\n")
            f.write(f"{content}\n")
        
        # Atomic move
        os.rename(temp_path, path)
        
    except Exception as e:
        log_fallback_failure(e)
        # Last resort: print to console
        print(f"FALLBACK SAVE FAILED: {e}")
        print(f"Content preview: {content[:100]}...")

def load_fallback_memories(fallback_dir, validate=True):
    """Load memories from fallback file storage with validation"""
    fallback_memories = []
    
    if not os.path.exists(fallback_dir):
        return fallback_memories
    
    for file in sorted(os.listdir(fallback_dir)):
        if file.endswith('.md') and not file.endswith('.tmp'):
            try:
                file_path = os.path.join(fallback_dir, file)
                
                # Check file size
                if os.path.getsize(file_path) > 1024 * 1024:  # 1MB limit
                    log_oversized_fallback(file_path)
                    continue
                
                with open(file_path, 'r') as f:
                    content = f.read()
                    
                # Validate if requested
                if validate and not validate_fallback_content(content):
                    log_invalid_fallback(file_path)
                    continue
                    
                fallback_memories.append({
                    'source': file,
                    'content': content,
                    'timestamp': os.path.getmtime(file_path)
                })
                
            except Exception as e:
                log_fallback_read_error(file, e)
                continue
    
    # Sort by timestamp (most recent first)
    fallback_memories.sort(key=lambda x: x['timestamp'], reverse=True)
    return fallback_memories[:10]  # Limit to 10 most recent
```

## Quality Assurance & Learning Integration

### Memory Quality Metrics:
- **Relevance Score**: How well memory matches current context (target >0.8)
- **Effectiveness Score**: Success rate of applied memory insights (target >85%)
- **Reusability Score**: How often memory is successfully applied across contexts (target >0.7)
- **Confidence Level**: Reliability of memory-based recommendations (target >0.75)
- **Learning Rate**: How quickly system improves from memory integration (target 5% monthly)

### Continuous Learning Process:
1. **Memory Application Tracking**: 
   - Monitor which memory insights are used and their outcomes
   - Track false positives/negatives in memory suggestions
   - Measure time saved through memory enhancement

2. **Effectiveness Analysis**: 
   - Compare success rates: memory-enhanced vs. standard operations
   - Identify memory categories with highest impact
   - Track user acceptance of memory-based suggestions

3. **Pattern Refinement**: 
   - Update successful patterns based on new outcomes
   - Consolidate similar patterns for efficiency
   - Elevate frequently used patterns to "best practices"

4. **Anti-Pattern Detection**: 
   - Identify and flag emerging failure modes
   - Create "avoid this" memories from failures
   - Alert on repeated mistake patterns

5. **User Adaptation**: 
   - Learn individual preferences and adapt memory surfacing
   - Personalize memory presentation style
   - Adjust confidence thresholds per user

### Memory Maintenance:

#### Automated Maintenance Tasks:
```python
def perform_memory_maintenance():
    """Execute regular memory maintenance operations"""
    
    # 1. Consolidation - Weekly
    if is_maintenance_due('consolidation', days=7):
        consolidate_similar_memories(similarity_threshold=0.9)
        extract_higher_patterns(min_occurrences=3)
    
    # 2. Validation - Daily
    if is_maintenance_due('validation', days=1):
        verify_memory_accuracy(sample_size=100)
        update_confidence_scores()
    
    # 3. Pruning - Monthly
    if is_maintenance_due('pruning', days=30):
        remove_outdated_memories(age_days=180, effectiveness_threshold=0.3)
        archive_low_use_memories(usage_threshold=2)
    
    # 4. Enhancement - Continuous
    enrich_memories_with_outcomes()
    update_memory_relationships()
    
    # 5. Cross-Reference - Weekly
    if is_maintenance_due('cross_reference', days=7):
        build_memory_graph()
        identify_memory_clusters()
```

## Success Metrics

### Immediate Success Indicators:
- Memory query response time <1000ms
- Relevant memories found rate >70%
- No sensitive data leakage (100% compliance)
- Successful fallback activation when needed

### Long-term Success Metrics:
- User productivity increase >20%
- Decision quality improvement >15%
- Pattern reuse rate >60%
- Zero memory-related security incidents

## Continuous Improvement

### Feedback Collection:
1. Track memory suggestion acceptance/rejection
2. Monitor memory-enhanced task completion times
3. Collect user satisfaction ratings
4. Analyze memory miss scenarios

### Improvement Actions:
- Refine memory schemas based on usage patterns
- Optimize query strategies for better relevance
- Enhance fallback mechanisms for reliability
- Update safety checks for emerging threats

### Review Triggers:
- Memory effectiveness drops below 70%
- User complaints about irrelevant suggestions
- New privacy regulations identified
- Performance degradation detected

## Memory Optimization Execution

### Performance Optimization Engine
```python
class MemoryOptimizationEngine:
    """Optimize memory operations for performance and relevance"""
    
    def __init__(self, memory_system, performance_monitor):
        self.memory = memory_system
        self.monitor = performance_monitor
        self.optimization_cache = {}
        self.performance_targets = {
            "query_latency": 1000,  # ms
            "relevance_score": 0.8,
            "cache_hit_rate": 0.7,
            "memory_usage": 100 * 1024 * 1024  # 100MB
        }
    
    def optimize_memory_queries(self, query_context):
        """Optimize queries for speed and relevance"""
        # 1. Query simplification
        optimized_query = self._simplify_query(query_context.original_query)
        
        # 2. Cache check
        cache_key = self._generate_cache_key(optimized_query, query_context)
        if cache_key in self.optimization_cache:
            cache_entry = self.optimization_cache[cache_key]
            if self._is_cache_valid(cache_entry):
                self.monitor.record_cache_hit()
                return cache_entry["results"]
        
        # 3. Parallel search strategy
        search_strategy = self._determine_search_strategy(optimized_query, query_context)
        
        # 4. Execute optimized search
        results = self._execute_parallel_search(search_strategy)
        
        # 5. Result optimization
        optimized_results = self._optimize_results(results, query_context)
        
        # 6. Update cache
        self._update_cache(cache_key, optimized_results)
        
        return optimized_results
    
    def _determine_search_strategy(self, query, context):
        """Determine optimal search strategy"""
        strategies = []
        
        # Exact match for recent memories
        strategies.append({
            "method": "exact_match",
            "query": query,
            "filters": {"recency": "7d", "relevance": ">0.9"},
            "limit": 5,
            "timeout": 200
        })
        
        # Semantic search for broader context
        strategies.append({
            "method": "semantic_search",
            "query": self._expand_query_semantically(query),
            "filters": {"relevance": ">0.7"},
            "limit": 10,
            "timeout": 500
        })
        
        # Pattern-based search
        if context.supports_patterns:
            strategies.append({
                "method": "pattern_search",
                "patterns": self._extract_patterns(query, context),
                "limit": 5,
                "timeout": 300
            })
        
        return strategies
    
    def _execute_parallel_search(self, strategies):
        """Execute searches in parallel for speed"""
        import concurrent.futures
        
        results = []
        with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
            # Submit all searches
            futures = []
            for strategy in strategies:
                future = executor.submit(
                    self._execute_single_search,
                    strategy
                )
                futures.append((future, strategy))
            
            # Collect results with timeout handling
            for future, strategy in futures:
                try:
                    result = future.result(timeout=strategy["timeout"] / 1000)
                    results.extend(result)
                except concurrent.futures.TimeoutError:
                    self.monitor.record_timeout(strategy["method"])
                except Exception as e:
                    self.monitor.record_error(strategy["method"], e)
        
        return results
    
    def optimize_memory_storage(self, content, context):
        """Optimize memory storage for efficiency"""
        # 1. Content compression
        compressed_content = self._compress_content(content)
        
        # 2. Intelligent indexing
        indexes = self._generate_indexes(content, context)
        
        # 3. Relationship mapping
        relationships = self._map_relationships(content, context)
        
        # 4. Storage strategy
        storage_strategy = {
            "primary": compressed_content,
            "indexes": indexes,
            "relationships": relationships,
            "ttl": self._calculate_ttl(content, context),
            "compression_ratio": len(compressed_content) / len(content)
        }
        
        return storage_strategy
    
    def perform_memory_maintenance(self):
        """Regular maintenance for optimal performance"""
        maintenance_tasks = []
        
        # 1. Cache optimization
        cache_stats = self._analyze_cache_performance()
        if cache_stats["hit_rate"] < self.performance_targets["cache_hit_rate"]:
            maintenance_tasks.append(self._optimize_cache_strategy())
        
        # 2. Index rebuilding
        if self._indexes_need_rebuild():
            maintenance_tasks.append(self._rebuild_indexes())
        
        # 3. Memory compaction
        if self._memory_fragmented():
            maintenance_tasks.append(self._compact_memory())
        
        # 4. Pattern cache refresh
        if self._pattern_cache_stale():
            maintenance_tasks.append(self._refresh_pattern_cache())
        
        return maintenance_tasks
```

### Adaptive Learning Optimizer
```python
class AdaptiveLearningOptimizer:
    """Continuously improve memory system performance"""
    
    def __init__(self, memory_system, analytics):
        self.memory = memory_system
        self.analytics = analytics
        self.learning_rate = 0.1
        self.optimization_history = []
    
    def learn_from_usage(self, usage_data):
        """Learn from actual usage patterns"""
        # 1. Analyze query patterns
        query_insights = self._analyze_query_patterns(usage_data["queries"])
        
        # 2. Analyze result effectiveness
        effectiveness_insights = self._analyze_result_effectiveness(usage_data["results"])
        
        # 3. Update optimization parameters
        self._update_optimization_parameters(query_insights, effectiveness_insights)
        
        # 4. Generate optimization recommendations
        recommendations = self._generate_optimization_recommendations(
            query_insights,
            effectiveness_insights
        )
        
        return recommendations
    
    def _analyze_query_patterns(self, queries):
        """Identify common query patterns for optimization"""
        patterns = {
            "common_terms": self._extract_common_terms(queries),
            "query_structures": self._identify_query_structures(queries),
            "time_patterns": self._analyze_temporal_patterns(queries),
            "user_patterns": self._analyze_user_patterns(queries)
        }
        
        # Identify optimization opportunities
        opportunities = []
        
        # Precompute common queries
        for term, frequency in patterns["common_terms"].items():
            if frequency > 10:  # Threshold for precomputation
                opportunities.append({
                    "type": "precompute",
                    "target": term,
                    "expected_improvement": frequency * 0.1  # 10% improvement per use
                })
        
        # Query template optimization
        for structure, count in patterns["query_structures"].items():
            if count > 5:
                opportunities.append({
                    "type": "template_optimization",
                    "structure": structure,
                    "optimization": self._optimize_query_structure(structure)
                })
        
        return {
            "patterns": patterns,
            "opportunities": opportunities
        }
    
    def _update_optimization_parameters(self, query_insights, effectiveness_insights):
        """Adaptively update system parameters"""
        # Update cache size based on hit patterns
        if effectiveness_insights["cache_effectiveness"] < 0.7:
            self._adjust_cache_size(increase=True)
        
        # Update search timeouts based on completion rates
        if effectiveness_insights["timeout_rate"] > 0.1:
            self._adjust_search_timeouts(increase=True)
        
        # Update relevance thresholds based on user feedback
        if effectiveness_insights["false_positive_rate"] > 0.2:
            self._adjust_relevance_threshold(increase=True)
        
        # Update index strategies based on query patterns
        if query_insights["patterns"]["index_misses"] > 0.3:
            self._update_indexing_strategy(query_insights["patterns"])
```

### Real-time Performance Monitor
```python
class MemoryPerformanceMonitor:
    """Monitor and optimize memory performance in real-time"""
    
    def __init__(self, memory_system):
        self.memory = memory_system
        self.metrics = {
            "query_latencies": [],
            "cache_hits": 0,
            "cache_misses": 0,
            "memory_usage": 0,
            "error_count": 0
        }
        self.alerts = []
    
    def monitor_operation(self, operation_type, operation_func, *args, **kwargs):
        """Monitor any memory operation"""
        start_time = time.time()
        start_memory = self._get_memory_usage()
        
        try:
            result = operation_func(*args, **kwargs)
            success = True
            error = None
        except Exception as e:
            result = None
            success = False
            error = e
            self.metrics["error_count"] += 1
        
        # Record metrics
        duration = (time.time() - start_time) * 1000  # ms
        memory_delta = self._get_memory_usage() - start_memory
        
        self._record_metrics({
            "operation": operation_type,
            "duration": duration,
            "memory_delta": memory_delta,
            "success": success,
            "error": error
        })
        
        # Check for performance issues
        self._check_performance_thresholds(operation_type, duration, memory_delta)
        
        return result
    
    def _check_performance_thresholds(self, operation, duration, memory_delta):
        """Alert on performance threshold violations"""
        # Latency alerts
        if duration > 1000:  # 1 second
            self.alerts.append({
                "type": "high_latency",
                "operation": operation,
                "duration": duration,
                "severity": "warning" if duration < 2000 else "critical"
            })
        
        # Memory alerts
        if memory_delta > 10 * 1024 * 1024:  # 10MB
            self.alerts.append({
                "type": "high_memory_usage",
                "operation": operation,
                "memory_delta": memory_delta,
                "severity": "warning"
            })
        
        # Error rate alerts
        error_rate = self.metrics["error_count"] / max(len(self.metrics["query_latencies"]), 1)
        if error_rate > 0.05:  # 5% error rate
            self.alerts.append({
                "type": "high_error_rate",
                "rate": error_rate,
                "severity": "critical"
            })
    
    def generate_performance_report(self):
        """Generate comprehensive performance report"""
        report = {
            "summary": {
                "avg_latency": statistics.mean(self.metrics["query_latencies"]) if self.metrics["query_latencies"] else 0,
                "p95_latency": self._calculate_percentile(self.metrics["query_latencies"], 95),
                "cache_hit_rate": self.metrics["cache_hits"] / max(self.metrics["cache_hits"] + self.metrics["cache_misses"], 1),
                "error_rate": self.metrics["error_count"] / max(len(self.metrics["query_latencies"]), 1),
                "memory_efficiency": self._calculate_memory_efficiency()
            },
            "alerts": self.alerts,
            "recommendations": self._generate_performance_recommendations()
        }
        
        return report
```

## Learning Feedback Loops

### Continuous Learning System
```python
class MemoryLearningSystem:
    """Implement continuous learning through feedback loops"""
    
    def __init__(self, memory_system, analytics_engine):
        self.memory = memory_system
        self.analytics = analytics_engine
        self.feedback_loops = self._initialize_feedback_loops()
        self.learning_metrics = {
            "decisions_improved": 0,
            "patterns_discovered": 0,
            "errors_prevented": 0,
            "optimizations_applied": 0
        }
    
    def _initialize_feedback_loops(self):
        """Setup feedback loops for different learning aspects"""
        return {
            "decision_outcome_loop": self.learn_from_decision_outcomes,
            "error_pattern_loop": self.learn_from_error_patterns,
            "user_interaction_loop": self.learn_from_user_interactions,
            "performance_optimization_loop": self.learn_from_performance_data,
            "workflow_effectiveness_loop": self.learn_from_workflow_results
        }
    
    def learn_from_decision_outcomes(self, decision_data):
        """Learn from the outcomes of decisions"""
        # 1. Capture decision and its outcome
        decision_memory = {
            "type": "decision_outcome",
            "decision": decision_data["decision"],
            "context": decision_data["context"],
            "predicted_outcome": decision_data.get("predicted_outcome"),
            "actual_outcome": decision_data["actual_outcome"],
            "outcome_delta": self._calculate_outcome_delta(
                decision_data.get("predicted_outcome"),
                decision_data["actual_outcome"]
            )
        }
        
        # 2. Update decision pattern confidence
        if decision_memory["outcome_delta"] < 0.2:  # Good prediction
            self._increase_pattern_confidence(decision_data["pattern_used"])
        else:  # Poor prediction
            self._decrease_pattern_confidence(decision_data["pattern_used"])
            self._analyze_prediction_failure(decision_memory)
        
        # 3. Create or update decision pattern
        self._update_decision_patterns(decision_memory)
        
        # 4. Generate learning insights
        insights = self._generate_decision_insights(decision_memory)
        
        return {
            "memory_created": decision_memory,
            "pattern_updates": self._get_pattern_updates(),
            "insights": insights,
            "learning_applied": True
        }
    
    def learn_from_error_patterns(self, error_data):
        """Learn from errors to prevent future occurrences"""
        # 1. Analyze error context
        error_analysis = {
            "error_type": error_data["type"],
            "error_context": error_data["context"],
            "root_cause": self._analyze_root_cause(error_data),
            "contributing_factors": self._identify_contributing_factors(error_data),
            "similar_errors": self._find_similar_errors(error_data)
        }
        
        # 2. Develop prevention strategy
        prevention_strategy = self._develop_prevention_strategy(error_analysis)
        
        # 3. Update error prevention patterns
        self._update_error_patterns({
            "error_signature": self._generate_error_signature(error_data),
            "prevention_strategy": prevention_strategy,
            "detection_rules": self._create_detection_rules(error_analysis)
        })
        
        # 4. Implement proactive warnings
        self._implement_proactive_warnings(prevention_strategy)
        
        self.learning_metrics["errors_prevented"] += 1
        
        return {
            "error_analysis": error_analysis,
            "prevention_strategy": prevention_strategy,
            "patterns_updated": True,
            "proactive_measures": "implemented"
        }
    
    def learn_from_user_interactions(self, interaction_data):
        """Learn from user behavior and preferences"""
        # 1. Analyze interaction patterns
        interaction_patterns = {
            "command_sequences": self._analyze_command_sequences(interaction_data),
            "preference_signals": self._extract_preference_signals(interaction_data),
            "feedback_patterns": self._analyze_feedback_patterns(interaction_data),
            "efficiency_metrics": self._calculate_efficiency_metrics(interaction_data)
        }
        
        # 2. Update user preference model
        preference_updates = self._update_user_preferences(interaction_patterns)
        
        # 3. Optimize interaction flows
        flow_optimizations = self._optimize_interaction_flows(interaction_patterns)
        
        # 4. Personalize responses
        personalization_updates = self._update_personalization_model(interaction_patterns)
        
        return {
            "patterns_learned": interaction_patterns,
            "preferences_updated": preference_updates,
            "optimizations_applied": flow_optimizations,
            "personalization_enhanced": personalization_updates
        }
    
    def learn_from_performance_data(self, performance_data):
        """Learn from system performance to optimize operations"""
        # 1. Identify performance bottlenecks
        bottlenecks = self._identify_bottlenecks(performance_data)
        
        # 2. Analyze successful optimizations
        successful_opts = self._analyze_successful_optimizations(performance_data)
        
        # 3. Update optimization strategies
        for bottleneck in bottlenecks:
            optimization = self._find_optimization_strategy(bottleneck, successful_opts)
            if optimization:
                self._apply_optimization(optimization)
                self.learning_metrics["optimizations_applied"] += 1
        
        # 4. Predict future performance issues
        predictions = self._predict_performance_issues(performance_data)
        
        return {
            "bottlenecks_identified": bottlenecks,
            "optimizations_applied": self.learning_metrics["optimizations_applied"],
            "performance_predictions": predictions,
            "system_improved": True
        }
    
    def aggregate_learning_insights(self):
        """Aggregate insights from all feedback loops"""
        insights = {
            "total_learnings": sum(self.learning_metrics.values()),
            "learning_distribution": self.learning_metrics,
            "pattern_evolution": self._analyze_pattern_evolution(),
            "system_intelligence_score": self._calculate_intelligence_score(),
            "improvement_trends": self._analyze_improvement_trends()
        }
        
        # Generate executive summary
        insights["executive_summary"] = self._generate_learning_summary(insights)
        
        return insights
```

### Feedback Integration Pipeline
```python
class FeedbackIntegrationPipeline:
    """Pipeline for integrating feedback into memory system"""
    
    def __init__(self, memory_system, learning_system):
        self.memory = memory_system
        self.learning = learning_system
        self.integration_queue = []
        self.processing_state = "idle"
    
    def process_feedback(self, feedback_type, feedback_data):
        """Process incoming feedback through appropriate channels"""
        # 1. Validate feedback
        if not self._validate_feedback(feedback_type, feedback_data):
            return {"status": "rejected", "reason": "validation_failed"}
        
        # 2. Enrich feedback with context
        enriched_feedback = self._enrich_feedback(feedback_type, feedback_data)
        
        # 3. Route to appropriate learning loop
        learning_result = self._route_to_learning_loop(feedback_type, enriched_feedback)
        
        # 4. Update memory system
        memory_updates = self._apply_memory_updates(learning_result)
        
        # 5. Propagate insights
        self._propagate_insights(learning_result["insights"])
        
        return {
            "status": "processed",
            "learning_applied": learning_result,
            "memory_updates": memory_updates,
            "insights_generated": len(learning_result.get("insights", []))
        }
    
    def batch_process_feedback(self, feedback_batch):
        """Process multiple feedback items efficiently"""
        results = []
        grouped_feedback = self._group_feedback_by_type(feedback_batch)
        
        for feedback_type, items in grouped_feedback.items():
            # Process similar feedback together for efficiency
            batch_result = self._process_feedback_batch(feedback_type, items)
            results.extend(batch_result)
        
        # Consolidate learnings
        consolidated = self._consolidate_batch_learnings(results)
        
        return consolidated
    
    def _route_to_learning_loop(self, feedback_type, feedback_data):
        """Route feedback to appropriate learning loop"""
        routing_map = {
            "decision_outcome": self.learning.learn_from_decision_outcomes,
            "error_report": self.learning.learn_from_error_patterns,
            "user_interaction": self.learning.learn_from_user_interactions,
            "performance_metric": self.learning.learn_from_performance_data,
            "workflow_result": self.learning.learn_from_workflow_results
        }
        
        if feedback_type in routing_map:
            return routing_map[feedback_type](feedback_data)
        else:
            # Generic learning path
            return self._generic_learning_process(feedback_type, feedback_data)
```

### Adaptive Intelligence Engine
```python
class AdaptiveIntelligenceEngine:
    """Core engine for adaptive memory intelligence"""
    
    def __init__(self, memory_system, learning_system, optimization_engine):
        self.memory = memory_system
        self.learning = learning_system
        self.optimizer = optimization_engine
        self.intelligence_state = self._initialize_intelligence_state()
    
    def evolve_intelligence(self):
        """Continuously evolve system intelligence"""
        evolution_cycle = {
            "current_intelligence": self._assess_current_intelligence(),
            "learning_opportunities": self._identify_learning_opportunities(),
            "evolution_strategies": self._develop_evolution_strategies(),
            "implementation_plan": self._create_implementation_plan()
        }
        
        # Execute evolution strategies
        for strategy in evolution_cycle["evolution_strategies"]:
            if strategy["confidence"] > 0.7:
                self._implement_evolution_strategy(strategy)
        
        # Measure evolution impact
        evolution_impact = self._measure_evolution_impact()
        
        return {
            "intelligence_evolved": True,
            "evolution_cycle": evolution_cycle,
            "impact_metrics": evolution_impact,
            "new_capabilities": self._identify_new_capabilities()
        }
    
    def _assess_current_intelligence(self):
        """Assess current state of system intelligence"""
        return {
            "pattern_recognition_accuracy": self._measure_pattern_accuracy(),
            "prediction_success_rate": self._measure_prediction_success(),
            "adaptation_speed": self._measure_adaptation_speed(),
            "learning_efficiency": self._measure_learning_efficiency(),
            "overall_intelligence_score": self._calculate_intelligence_score()
        }
    
    def _identify_learning_opportunities(self):
        """Identify areas for intelligence improvement"""
        opportunities = []
        
        # Analyze failure patterns
        failures = self._analyze_system_failures()
        for failure in failures:
            opportunities.append({
                "type": "failure_learning",
                "area": failure["domain"],
                "potential_improvement": failure["improvement_potential"],
                "learning_approach": self._suggest_learning_approach(failure)
            })
        
        # Analyze success patterns for optimization
        successes = self._analyze_system_successes()
        for success in successes:
            if success["optimization_potential"] > 0.2:
                opportunities.append({
                    "type": "success_optimization",
                    "area": success["domain"],
                    "potential_improvement": success["optimization_potential"],
                    "optimization_approach": self._suggest_optimization_approach(success)
                })
        
        return sorted(opportunities, key=lambda o: o["potential_improvement"], reverse=True)
```

## Final Integration Summary

The enhanced memory operations task now includes:

1. **Memory Integration Patterns** for each operation type (decisions, implementations, workflows, consultations)
2. **Proactive Intelligence Hooks** that trigger memory surfacing based on context
3. **Pattern Recognition Integration** with advanced pattern analysis and cross-referencing
4. **Cross-Session Continuity Mechanisms** to maintain context and momentum
5. **Memory Optimization Execution** with performance monitoring and adaptive optimization
6. **Learning Feedback Loops** that continuously improve the system through experience

All enhancements build upon the existing safety rules from Story 4, maintaining:
- Mandatory safety validations
- Progressive disclosure phases
- Comprehensive error handling
- Fallback mechanisms
- Quality gates and metrics

The system now provides a complete memory-enhanced operation framework that learns and improves over time while maintaining strict safety and quality standards.