# What's Changed Template

## 🔄 Welcome Back!

**Time Away**: {time_duration}  
**Last Active**: {last_activity_timestamp}  
**Project**: {project_name}  

---

## 📊 Progress While You Were Away

### Overall Project
- **Sprint Progress**: Day {current_day} of {sprint_length}
- **Completion**: {old_percentage}% → {new_percentage}% ({change_indicator})
- **Velocity**: {velocity_indicator}

### Your Work
- **Status**: {your_work_status}
- **Blockers Resolved**: {resolved_count}
- **New Dependencies**: {new_dependencies}

---

## 🔔 Key Updates

### 📝 Code Changes
{if_commits_exist}
**New Commits** ({commit_count}):
1. {commit_type}: {commit_message} - {author}
2. {commit_type}: {commit_message} - {author}
3. {more_commits_indicator}

💡 **Impact on your work**: {impact_assessment}
{else}
✅ No code changes - repository stable
{endif}

### 👥 Team Activity
{if_team_updates}
- **{team_member}**: {activity_summary}
- **{team_member}**: {activity_summary}
{else}
ℹ️ No significant team updates
{endif}

### 🎯 Priority Shifts
{if_priority_changes}
⚠️ **New High Priority**: {item_description}
🔄 **Reprioritized**: {item_description}
{else}
✅ Priorities remain unchanged
{endif}

---

## 💡 Contextual Insights

### From Memory Patterns
Based on {similar_situation_count} similar situations:
- **Common Next Step**: {predicted_next_action}
- **Watch Out For**: {potential_issue}
- **Success Pattern**: {relevant_pattern}

### Personalized Recommendations
Given your working style and current context:
1. {personalized_recommendation_1}
2. {personalized_recommendation_2}
3. {personalized_recommendation_3}

---

## ⚡ Quick Actions

### Continue Your Work
```
/continue              # Resume {last_task_name}
/continue --latest     # Start from latest changes
/continue --review     # Review changes first
```

### Catch Up Options
```
/review commits        # Detailed commit review
/review decisions      # See team decisions
/review blockers       # Check resolved/new blockers
```

### Alternative Paths
```
/suggest              # Get fresh recommendations
/switch {task}        # Change focus
/handoff {persona}    # Different perspective needed
```

---

## 📅 Time-Sensitive Items

{if_deadlines}
### ⏰ Upcoming Deadlines
1. **{deadline_item}** - Due in {time_remaining}
2. **{deadline_item}** - Due in {time_remaining}

### 🚨 Urgent Actions
- {urgent_action_1}
- {urgent_action_2}
{else}
✅ No urgent items requiring immediate attention
{endif}

---

## 🔍 Detailed Change Log

<details>
<summary>Click to expand full change details</summary>

### File Changes
```
{file_change_summary}
```

### Configuration Updates
```
{config_changes}
```

### Dependency Updates
```
{dependency_changes}
```

### Test Results
```
{test_status_changes}
```

</details>

---

## 🎯 Suggested Next Steps

Based on context analysis and patterns:

1. **Immediate** (< 30 min):
   - {immediate_action}
   - {immediate_action}

2. **Short-term** (Today):
   - {short_term_action}
   - {short_term_action}

3. **Planning Required**:
   - {planning_item}
   - {planning_item}

---

**Ready to continue?** Type `/continue` or choose a specific action above.  
**Need more details?** Try `/review [topic]` or ask any question.

*Generated at {timestamp} | Context confidence: {confidence_score}%*