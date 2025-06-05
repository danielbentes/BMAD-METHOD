# Emergency Handoff Task

## Purpose
Enable rapid, focused persona transitions during crisis situations where standard handoff protocols would cause unacceptable delays. Prioritize immediate action capability over comprehensive context transfer.

## Emergency Triggers
- Critical production issues requiring immediate response
- Key team member sudden unavailability
- Time-sensitive decisions with approaching deadlines
- External crisis requiring rapid role changes
- System failures demanding specialized expertise

## Emergency Handoff Protocol

### Phase 1: Rapid Assessment (30 seconds)
```python
def assess_emergency_severity(situation):
    """Quickly determine handoff urgency and scope"""
    
    severity_indicators = {
        "production_down": "critical",
        "data_breach": "critical",
        "key_person_unavailable": "high",
        "deadline_approaching": "high",
        "stakeholder_escalation": "medium"
    }
    
    # Determine time available
    if "immediate" in situation or "now" in situation:
        time_budget = "2_minutes"
    elif "urgent" in situation or "asap" in situation:
        time_budget = "5_minutes"
    else:
        time_budget = "10_minutes"
    
    return {
        "severity": determine_severity(situation, severity_indicators),
        "time_budget": time_budget,
        "handoff_mode": "emergency"
    }
```

### Phase 2: Critical Context Extraction (1 minute)
```python
def extract_critical_context(current_state, time_budget):
    """Extract only the most critical information"""
    
    if time_budget == "2_minutes":
        return {
            "crisis_description": current_state.active_crisis,
            "immediate_actions_needed": current_state.next_24h_critical,
            "decision_authority": current_state.decision_boundaries,
            "key_contacts": current_state.emergency_contacts[:3]
        }
    elif time_budget == "5_minutes":
        # Include slightly more context
        critical_context = extract_2_minute_context()
        critical_context.update({
            "recent_actions": current_state.last_48h_summary,
            "active_blockers": current_state.blockers[:5],
            "resource_access": current_state.critical_resources
        })
        return critical_context
    else:
        # 10-minute version includes more background
        return extract_standard_emergency_context(current_state)
```

### Phase 3: Emergency Handoff Execution

#### 2-Minute Emergency Handoff Template
```markdown
# 🚨 EMERGENCY HANDOFF: {Source} → {Target}

## CRISIS SITUATION
**What's Happening**: {crisis_one_liner}
**Impact**: {who_what_affected}
**Your Role**: {specific_responsibility}

## IMMEDIATE ACTIONS (Next 2 Hours)
1. ⚡ {action_1} - {why_critical}
2. ⚡ {action_2} - {why_critical}
3. ⚡ {action_3} - {why_critical}

## DECISION AUTHORITY
✅ You CAN: {authorized_decisions}
❌ You CANNOT: {requires_escalation}
🤝 Escalate to: {escalation_contact}

## EMERGENCY CONTACTS
1. {contact_1_role}: {name} - {phone} - {when_to_call}
2. {contact_2_role}: {name} - {phone} - {when_to_call}
3. {contact_3_role}: {name} - {phone} - {when_to_call}

## CRITICAL RESOURCES
- System Access: {access_link_or_location}
- Documentation: {emergency_runbook_location}
- Status Page: {where_to_update_status}

CONFIRMATION REQUIRED: "I understand and am taking over" ⬇️
```

#### 5-Minute Emergency Handoff Template
```markdown
# 🚨 EMERGENCY HANDOFF: {Source} → {Target}

## SITUATION OVERVIEW
**Crisis**: {detailed_crisis_description}
**Started**: {when_issue_began}
**Current Status**: {red|yellow|stabilizing}
**Business Impact**: {specific_impacts}

## YOUR IMMEDIATE RESPONSIBILITIES
**Primary Mission**: {main_objective}
**Success Criteria**: {how_to_know_its_resolved}
**Time Constraint**: {deadline_if_any}

## ACTIONS TAKEN SO FAR
- ✅ {completed_action_1} - {result}
- ✅ {completed_action_2} - {result}
- ⏳ {in_progress_action} - {status}
- ❌ {failed_attempt} - {why_failed}

## NEXT CRITICAL STEPS
### Next 2 Hours (CRITICAL)
1. {urgent_task_1}
   - Why: {reason}
   - How: {brief_instruction}
   - Success: {success_indicator}

2. {urgent_task_2}
   - Why: {reason}
   - How: {brief_instruction}
   - Success: {success_indicator}

### Next 24 Hours (IMPORTANT)
- {important_task_1}
- {important_task_2}
- {important_task_3}

## DECISION FRAMEWORK
### You Have Authority To:
- {decision_type_1} up to {limit}
- {decision_type_2} for {scope}
- {decision_type_3} except {exception}

### Requires Escalation:
- {escalation_trigger_1} → Contact {person}
- {escalation_trigger_2} → Contact {person}

## ACTIVE BLOCKERS
1. 🚧 {blocker_1}
   - Impact: {what_it_blocks}
   - Workaround: {temporary_solution}
   - Resolution: {who_is_working_on_it}

## RESOURCE QUICK REFERENCE
### Systems & Access
- Production: {prod_access}
- Monitoring: {monitoring_dashboard}
- Logs: {log_location}
- Runbooks: {runbook_location}

### Key People
| Role | Name | Contact | Availability |
|------|------|---------|--------------|
| {role_1} | {name} | {contact} | {when_available} |
| {role_2} | {name} | {contact} | {when_available} |
| {role_3} | {name} | {contact} | {when_available} |

## MEMORY INSIGHTS (If Available)
⚡ **Similar Crisis Pattern**: {pattern_description}
💡 **What Worked Before**: {successful_approach}
⚠️ **Common Pitfall**: {what_to_avoid}

## STATUS COMMUNICATION
- Update Channel: {where_to_post_updates}
- Update Frequency: Every {frequency}
- Stakeholders Expecting Updates: {list}

READY TO PROCEED? Confirm with specific action you're taking first ⬇️
```

### Phase 4: Rapid Validation (30 seconds)
```markdown
## ⚡ QUICK VALIDATION

Target Persona Response Required:
1. "I understand the situation: {one_line_summary}"
2. "My first action will be: {specific_action}"
3. "I'll escalate to {person} if: {condition}"

✅ HANDOFF COMPLETE when all 3 confirmed
```

## Emergency Handoff Patterns

### Pattern 1: Production Crisis
**Trigger**: System down, data loss, security breach
**Focus**: Immediate mitigation and communication
**Key Elements**:
- System status and impact scope
- Mitigation actions in progress
- Communication channels active
- Escalation thresholds clear

### Pattern 2: Key Person Unavailable
**Trigger**: Illness, emergency, unexpected absence
**Focus**: Coverage of critical responsibilities
**Key Elements**:
- Today's critical meetings/decisions
- Pending approvals or blockers
- Stakeholder expectations
- Access to necessary resources

### Pattern 3: Time-Critical Decision
**Trigger**: Deadline approaching, external pressure
**Focus**: Decision context and authority
**Key Elements**:
- Decision options and implications
- Stakeholder positions
- Decision criteria
- Approval process

### Pattern 4: External Crisis
**Trigger**: Customer escalation, PR issue, legal matter
**Focus**: Response coordination and messaging
**Key Elements**:
- Current situation and trajectory
- Approved messaging
- Response team contacts
- Legal/compliance constraints

## Memory Integration for Emergencies

### Pre-Cached Emergency Patterns
```python
def cache_emergency_patterns():
    """Pre-load common emergency scenarios for fast access"""
    
    cached_patterns = {
        "production_down": load_pattern("production_crisis_response"),
        "security_incident": load_pattern("security_breach_protocol"),
        "key_person_out": load_pattern("coverage_protocols"),
        "pr_crisis": load_pattern("external_communication_crisis")
    }
    
    return cached_patterns
```

### Rapid Memory Query
```python
def emergency_memory_search(crisis_type, time_limit=2):
    """Fast memory search with timeout"""
    
    try:
        # Use pre-cached patterns first
        if crisis_type in cached_patterns:
            return cached_patterns[crisis_type]
        
        # Quick memory search with strict timeout
        results = search_memory(
            f"emergency {crisis_type} resolution",
            limit=3,
            timeout=time_limit * 1000  # milliseconds
        )
        return results
    except TimeoutError:
        # Return generic emergency guidance
        return get_generic_emergency_guidance(crisis_type)
```

## Post-Emergency Protocol

### Immediate Post-Crisis (First 2 hours)
1. **Stabilization Confirmation**
   - Verify crisis contained
   - Document immediate actions taken
   - Identify follow-up requirements

2. **Stakeholder Communication**
   - Send "all-clear" or status update
   - Schedule debrief meetings
   - Update status pages

### Recovery Phase (24-48 hours)
1. **Full Context Restoration**
   - Conduct proper handoff if needed
   - Document crisis timeline
   - Update runbooks

2. **Learning Capture**
   ```python
   def capture_emergency_learning(crisis_event):
       learning_entry = {
           "crisis_type": crisis_event.type,
           "trigger": crisis_event.trigger,
           "response_time": crisis_event.response_metrics,
           "what_worked": crisis_event.successful_actions,
           "what_failed": crisis_event.failed_attempts,
           "improvement_suggestions": crisis_event.lessons_learned,
           "handoff_effectiveness": crisis_event.handoff_score
       }
       
       add_memory(
           content=learning_entry,
           category="emergency-response",
           tags=["crisis", crisis_event.type, "handoff"]
       )
   ```

## Success Metrics

### Emergency Handoff KPIs
- Time to first action: <5 minutes
- Crisis recognition accuracy: >95%
- Handoff completion time: <configured_budget
- Post-crisis productivity: >80% normal

### Quality Indicators
- Clear crisis understanding demonstrated
- Correct first action identified
- Appropriate escalation awareness
- No critical information gaps

## Common Emergency Scenarios

### Scenario 1: Database Corruption
```markdown
CRISIS: Production database corruption detected
IMPACT: 50K users affected, transactions failing
YOUR ROLE: Stop corruption spread, initiate recovery

IMMEDIATE ACTIONS:
1. ⚡ Set database to read-only mode
2. ⚡ Initiate snapshot backup
3. ⚡ Alert data team lead

AUTHORITY: Can halt all writes, cannot delete data
ESCALATE TO: DBA on-call: +1-555-0911
```

### Scenario 2: CEO Request
```markdown
CRISIS: CEO needs board presentation update in 2 hours
IMPACT: Board meeting decision depends on data
YOUR ROLE: Gather metrics and update slides

IMMEDIATE ACTIONS:
1. ⚡ Pull latest KPIs from dashboard
2. ⚡ Update slides 5-8 with new data
3. ⚡ Send to CEO for review

AUTHORITY: Access all metric systems
ESCALATE TO: CFO if financial data needed
```

## Tool Integration

### Emergency Commands
```bash
# Trigger emergency handoff
/handoff {persona} --emergency

# With time constraint
/handoff {persona} --emergency --time=2min

# With specific crisis type
/handoff {persona} --emergency --crisis=production-down

# Skip validation for extreme urgency
/handoff {persona} --emergency --skip-validation
```

### System Support
- Auto-detection of crisis keywords
- Pre-loaded emergency contacts
- Cached runbook locations
- Rapid access permission elevation

## Continuous Improvement

### Emergency Response Review
- Weekly review of emergency handoffs
- Response time analysis
- Effectiveness scoring
- Pattern updates

### Runbook Maintenance
- Monthly validation of emergency procedures
- Contact list updates
- Access permission reviews
- Tool availability checks

This emergency protocol ensures rapid response capability while maintaining minimum viable context for effective crisis management.