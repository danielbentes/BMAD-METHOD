# Memory Visualization Template

## 🧠 Memory System Dashboard

### 📊 Memory Statistics
**Total Memories**: {total_count}  
**Last Updated**: {last_update_timestamp}  
**Active Project**: {current_project_name}

#### Category Breakdown
```
Decisions       ████████████░░░░ {decision_count} ({decision_percentage}%)
Patterns        ██████████░░░░░░ {pattern_count} ({pattern_percentage}%)
Implementations ████████░░░░░░░░ {implementation_count} ({implementation_percentage}%)
Consultations   ██████░░░░░░░░░░ {consultation_count} ({consultation_percentage}%)
User Preferences ████░░░░░░░░░░░ {preference_count} ({preference_percentage}%)
Mistakes        ███░░░░░░░░░░░░░ {mistake_count} ({mistake_percentage}%)
Quality Metrics ████░░░░░░░░░░░░ {quality_count} ({quality_percentage}%)
```

### 🔥 Most Active Categories
1. **{top_category_1}**: {top_category_1_activity} memories/week
2. **{top_category_2}**: {top_category_2_activity} memories/week
3. **{top_category_3}**: {top_category_3_activity} memories/week

---

## 🎯 Recent Patterns
*Patterns identified from your memory bank with confidence scores*

### High Confidence Patterns (>80%)
{#if high_confidence_patterns}
#### 1. {pattern_1_name} (Confidence: {pattern_1_confidence}%)
- **Type**: {pattern_1_type}
- **Occurrences**: {pattern_1_count} times
- **Success Rate**: {pattern_1_success}%
- **Key Insight**: {pattern_1_insight}
- **Apply When**: {pattern_1_context}

#### 2. {pattern_2_name} (Confidence: {pattern_2_confidence}%)
- **Type**: {pattern_2_type}
- **Occurrences**: {pattern_2_count} times
- **Success Rate**: {pattern_2_success}%
- **Key Insight**: {pattern_2_insight}
- **Apply When**: {pattern_2_context}
{else}
*No high-confidence patterns identified yet. Continue documenting your work to build patterns.*
{/if}

### Emerging Patterns (50-80%)
{#if emerging_patterns}
🔄 **{emerging_pattern_name}** (Confidence: {emerging_confidence}%)
- Seen {emerging_count} times
- Needs {emerging_needed} more occurrences to establish
- Early indicator: {emerging_indicator}
{else}
*No emerging patterns detected*
{/if}

---

## 💡 Actionable Insights
*AI-generated recommendations based on your memory patterns*

### 🚨 Priority Insights
{#if priority_insights}
1. **{insight_1_title}**
   - 📊 Based on: {insight_1_evidence_count} similar situations
   - 🎯 Action: {insight_1_action}
   - ⏱️ Timing: {insight_1_timing}
   - 📈 Expected Impact: {insight_1_impact}

2. **{insight_2_title}**
   - 📊 Based on: {insight_2_evidence_count} similar situations
   - 🎯 Action: {insight_2_action}
   - ⏱️ Timing: {insight_2_timing}
   - 📈 Expected Impact: {insight_2_impact}
{else}
*Gathering more data to generate insights. Keep using /remember to build your knowledge base.*
{/if}

### 💭 Contextual Suggestions
Based on your current work on **{current_task}**:
- 🔍 Similar past situation: {similar_situation_summary}
- ✅ What worked: {what_worked}
- ❌ What to avoid: {what_to_avoid}
- 💡 Consider: {contextual_suggestion}

---

## 📈 Memory Quality Metrics

### Coverage Score: {coverage_score}/100
How well your memories cover different aspects of your work:
```
Technical Decisions  ████████████░░░░ {tech_coverage}%
Process Workflows    ██████████░░░░░░ {process_coverage}%
Team Collaboration   ████████░░░░░░░░ {team_coverage}%
Quality Practices    ██████░░░░░░░░░░ {quality_coverage}%
```

### Memory Effectiveness
- **Recall Success Rate**: {recall_success}% - How often recalled memories are relevant
- **Pattern Application**: {pattern_application}% - How often patterns are successfully applied
- **Insight Accuracy**: {insight_accuracy}% - How often insights lead to positive outcomes

---

## 🔍 Recent Memory Activity

### Last 5 Memories Added
{#each recent_memories}
{memory_index}. **{memory_timestamp}** - {memory_category}
   ```
   {memory_summary}
   ```
   Tags: {memory_tags}
{/each}

### Most Recalled Memories (Last 7 Days)
{#each popular_memories}
- **{popular_memory_title}** (recalled {recall_count} times)
  - Context: {popular_memory_context}
  - Value: {popular_memory_value}
{/each}

---

## 🎨 Memory Graph Visualization

### Relationship Network
```
                    [Current Context]
                           |
            +--------------+--------------+
            |              |              |
      [Decisions]    [Patterns]    [Insights]
            |              |              |
      +---------+    +---------+    +---------+
      |    |    |    |    |    |    |    |    |
   [D1] [D2] [D3]  [P1] [P2] [P3]  [I1] [I2] [I3]
```

### Memory Timeline
```
Week 1  ████████░░░░░░░░░░░░ {week1_count} memories
Week 2  ████████████░░░░░░░░ {week2_count} memories  
Week 3  ████████████████░░░░ {week3_count} memories
Week 4  ████████████████████ {week4_count} memories ← Current
```

---

## 🛠️ Memory Management

### Quick Actions
- `/remember` - Add new memory
- `/recall {query}` - Search memories
- `/patterns` - View all patterns
- `/insights` - Get fresh insights
- `/learn {outcome}` - Capture learning

### Memory Health
{#if memory_health_good}
✅ **Healthy** - Memory system operating normally
- Storage: {storage_used}MB / {storage_limit}MB
- Performance: {query_speed}ms average query time
- Integrity: No corruption detected
{else}
⚠️ **Attention Needed**
- {health_issue_1}
- {health_issue_2}
Recommended: {health_recommendation}
{/if}

### Optimization Suggestions
{#if has_optimization_suggestions}
1. **{optimization_1_title}**
   - Current: {optimization_1_current}
   - Suggested: {optimization_1_suggested}
   - Benefit: {optimization_1_benefit}

2. **{optimization_2_title}**
   - Current: {optimization_2_current}
   - Suggested: {optimization_2_suggested}
   - Benefit: {optimization_2_benefit}
{else}
✨ Your memory usage is well-optimized!
{/if}

---

## 📚 Learning Progress

### Knowledge Growth
```
Month 1 ██░░░░░░░░░░░░░░░░░░ 10% - Foundation Building
Month 2 ██████░░░░░░░░░░░░░░ 30% - Pattern Recognition
Month 3 ████████████░░░░░░░░ 60% - Insight Generation ← You are here
Month 4 ████████████████████ 100% - Mastery Level
```

### Milestones Achieved
- ✅ First 100 memories
- ✅ First recognized pattern
- ✅ First successful pattern application
- ⏳ First cross-project insight
- ⏳ Memory-driven workflow optimization

### Next Learning Goals
1. Add {memories_needed_for_next_pattern} more memories to establish "{pending_pattern_name}" pattern
2. Apply "{ready_pattern_name}" pattern to current work
3. Document outcome of "{recent_decision_name}" decision

---

*Memory visualization generated at {timestamp}*  
*Based on {total_memory_count} memories across {project_count} projects*  
*System confidence: {system_confidence}%*