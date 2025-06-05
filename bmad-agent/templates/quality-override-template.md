# Quality Gate Override Request

## Override Request Details
**Request ID**: {override_request_id}  
**Requested By**: {requester_name}  
**Role**: {requester_role}  
**Date**: {request_date}  
**Gate to Override**: {gate_name}  
**Current Phase**: {phase}  
**Enforcement Level**: {enforcement_level}

## ⚠️ Override Authority Requirements

| Gate Type | Required Authority | Current Requester | Authorized |
|-----------|-------------------|-------------------|------------|
| {gate_type} | {required_role} | {requester_role} | {yes/no} |

**Override Allowed**: {override_permission_status}  
**Reason**: {permission_reason}

## 📋 Failed Gate Summary

### Blocking Issues
Total Failed Checks: {failed_check_count}

| Check | Severity | Current Value | Required Value | Gap |
|-------|----------|---------------|----------------|------|
| {check_1} | {severity_1} | {current_1} | {required_1} | {gap_1} |
| {check_2} | {severity_2} | {current_2} | {required_2} | {gap_2} |
| {check_3} | {severity_3} | {current_3} | {required_3} | {gap_3} |

### Impact Analysis
**Immediate Impact**: {immediate_impact_description}  
**Downstream Risk**: {downstream_risk_description}  
**Technical Debt Created**: {technical_debt_estimate}

## 📝 Business Justification

### Primary Justification
{business_justification_text}

### Supporting Context
- **Business Driver**: {business_driver}
- **Timeline Constraint**: {timeline_reason}
- **Customer Impact**: {customer_impact_if_delayed}
- **Revenue Impact**: {revenue_impact_if_delayed}

### Alternative Considered
**Option Evaluated**: {alternative_option}  
**Why Rejected**: {rejection_reason}  
**Time Required**: {alternative_time_estimate}

## 🛡️ Risk Assessment

### Risk Matrix
| Risk Category | Probability | Impact | Mitigation Strategy |
|---------------|-------------|---------|-------------------|
| Security | {sec_prob} | {sec_impact} | {sec_mitigation} |
| Performance | {perf_prob} | {perf_impact} | {perf_mitigation} |
| Stability | {stab_prob} | {stab_impact} | {stab_mitigation} |
| Maintainability | {maint_prob} | {maint_impact} | {maint_mitigation} |

### Overall Risk Score
**Calculated Risk**: {risk_score}/100  
**Risk Level**: {risk_level}  
**Acceptable Threshold**: {acceptable_threshold}

## 📅 Remediation Plan

### Remediation Timeline
**Commitment Date**: {remediation_deadline}  
**Sprint Allocation**: {sprint_number}  
**Story Created**: {story_id}

### Remediation Tasks
1. **{task_1}**
   - Owner: {owner_1}
   - Due: {due_1}
   - Verification: {verification_1}

2. **{task_2}**
   - Owner: {owner_2}
   - Due: {due_2}
   - Verification: {verification_2}

3. **{task_3}**
   - Owner: {owner_3}
   - Due: {due_3}
   - Verification: {verification_3}

### Success Criteria
Post-remediation, the following must be true:
- [ ] {success_criterion_1}
- [ ] {success_criterion_2}
- [ ] {success_criterion_3}
- [ ] All original gate checks passing

## 👤 Accountability Assignment

### Primary Accountability
**Accountable Individual**: {accountable_person}  
**Role**: {accountable_role}  
**Contact**: {accountable_contact}

### Escalation Path
1. **First Level**: {escalation_1} (if remediation delayed)
2. **Second Level**: {escalation_2} (if risk materializes)
3. **Executive**: {escalation_3} (if critical issue occurs)

### Review Schedule
- **Daily Check**: Until remediation complete
- **Weekly Review**: With {reviewer}
- **Gate Re-check**: {recheck_date}

## 📊 Historical Context

### Similar Override History
| Date | Gate | Reason | Remediation Time | Outcome |
|------|------|---------|------------------|----------|
| {date_1} | {gate_1} | {reason_1} | {time_1} | {outcome_1} |
| {date_2} | {gate_2} | {reason_2} | {time_2} | {outcome_2} |

### Team Override Metrics
- **Override Frequency**: {team_override_rate}% of gates
- **Average Remediation Time**: {avg_remediation_days} days
- **On-Time Remediation**: {on_time_percentage}%

## ✅ Approval Decision

### Approval Status: {APPROVED/DENIED/PENDING}

### Conditions of Approval (if approved)
1. **Remediation Deadline**: Hard deadline of {deadline}
2. **Daily Updates**: Required until resolved
3. **No Additional Overrides**: Until this is remediated
4. **Escalation Trigger**: Auto-escalate if missed deadline

### Approval Chain
- **Submitted**: {submitted_timestamp}
- **Tech Lead Review**: {tech_lead_approval} at {tl_timestamp}
- **Architect Review**: {architect_approval} at {arch_timestamp}
- **PM Approval**: {pm_approval} at {pm_timestamp}

### Denial Reason (if denied)
{denial_reason_text}

### Next Steps (if denied)
1. {required_action_1}
2. {required_action_2}
3. {required_action_3}

## 🔄 Tracking Information

### Override Record
```yaml
override_record:
  id: {override_id}
  gate: {gate_name}
  requester: {requester}
  approved_by: {approver}
  timestamp: {timestamp}
  remediation_due: {due_date}
  technical_debt_id: {debt_ticket_id}
  status: {active/remediated/expired}
```

### Automated Tracking
- **Debt Ticket**: Automatically created at {ticket_link}
- **Calendar Reminder**: Set for {reminder_date}
- **Gate Re-check**: Scheduled for {recheck_date}
- **Metrics Update**: Override logged in team metrics

## 📝 Accountability Statement

By approving this override, I acknowledge:
- The identified risks and accept responsibility for outcomes
- The remediation timeline is binding and will be met
- Daily updates will be provided until remediation is complete
- This override will be tracked in team quality metrics
- Future overrides may be restricted if remediation is delayed

**Digital Signature**: {approver_name}  
**Date**: {approval_date}  
**Override Expiry**: {expiry_date}

---

**Important**: This override is valid only for the specific gate and context described above. Any changes to scope or timeline require a new override request. Failure to meet remediation commitments will result in escalation and potential restriction of future override privileges.