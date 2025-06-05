# Bootstrap Dialogue Template - Interactive Mode

## Purpose
This template provides structured dialogue prompts for interactive memory bootstrap sessions. The LLM should use these prompts to guide users through the bootstrap process while gathering additional context and validation.

## Dialogue Flow

### 1. Bootstrap Initiation
```
🧠 Welcome to BMAD Memory Bootstrap - Interactive Mode

I'll analyze your codebase and create foundational memories to enhance our collaboration.
This process typically takes 30-45 minutes and will help me understand:
- Your architectural decisions and rationale
- Coding patterns and conventions
- Team preferences and workflows
- Known issues and solutions

Ready to begin? (yes/no/tell me more)
```

### 2. Project Context Gathering
```
📋 Let's start with some context about your project:

1. What type of project is this? (e.g., web app, API, mobile app, library)
2. What's the primary business domain? (e.g., e-commerce, healthcare, finance)
3. How long has this project been in development?
4. How many people typically work on this codebase?
5. What's your role in this project?

(You can answer all at once or one by one)
```

### 3. Technology Stack Confirmation
```
🔍 I've detected the following technology stack:

Frontend: {detected_frontend}
Backend: {detected_backend}
Database: {detected_database}
Testing: {detected_testing}
Build Tools: {detected_build}

Is this accurate? Are there any key technologies I missed?
```

### 4. Architecture Discovery
```
🏗️ I've identified what appears to be a {architecture_pattern} architecture.

Key structural patterns I see:
- {pattern_1}
- {pattern_2}
- {pattern_3}

Does this match your understanding? Any important architectural decisions I should know about?
```

### 5. Decision Validation Loop
```
💡 I found evidence of this architectural decision:

**Decision**: {decision_summary}
**Apparent Rationale**: {inferred_rationale}
**Confidence**: {confidence}%

Questions:
1. Is this decision still active/relevant?
2. What was the main driver for this choice?
3. Were there specific constraints that influenced this?
4. Any lessons learned from this decision?
```

### 6. Pattern Recognition Dialogue
```
🔄 I've noticed this recurring pattern:

**Pattern**: {pattern_name}
**Found in**: {location_count} locations
**Example**: {code_snippet}

Is this an intentional pattern you want to preserve? 
What makes this approach effective for your team?
```

### 7. Issue/Challenge Discussion
```
🚨 I've identified a potential challenge area:

**Issue**: {issue_description}
**Current Handling**: {how_its_handled}
**Impact**: {impact_assessment}

Questions:
1. Is this a known issue the team is tracking?
2. Are there plans to address this?
3. What's prevented fixing this so far?
4. Should I document any workarounds you use?
```

### 8. Preference Extraction
```
👥 Let's capture some team preferences:

Based on the code, I see you prefer:
- {preference_1}
- {preference_2}
- {preference_3}

Are these deliberate choices? 
What other coding/workflow preferences should I remember?
```

### 9. Priority Setting
```
🎯 From what I've learned, here are potential focus areas:

1. {area_1} - {why_important}
2. {area_2} - {why_important}
3. {area_3} - {why_important}

Which of these aligns best with your current priorities?
What would you like me to pay special attention to going forward?
```

### 10. Memory Creation Confirmation
```
📝 I'm ready to create the following memories:

**Decisions** ({count}):
- {decision_preview_1}
- {decision_preview_2}

**Patterns** ({count}):
- {pattern_preview_1}
- {pattern_preview_2}

**Preferences** ({count}):
- {preference_preview_1}
- {preference_preview_2}

Should I proceed with creating these memories? Any adjustments needed?
```

### 11. Custom Deep Dive Options
```
🔬 Would you like me to analyze any specific areas more deeply?

Options:
1. Security patterns and practices
2. Performance optimizations
3. Testing strategies
4. API design patterns
5. Error handling approaches
6. Something else?

(Enter number or describe what you'd like me to focus on)
```

### 12. Bootstrap Completion
```
✅ Bootstrap Complete!

I've created {total_memories} memories across {category_count} categories:
- Decisions: {decision_count}
- Patterns: {pattern_count}
- Preferences: {preference_count}
- Issues: {issue_count}

**Key Insights**:
1. {key_insight_1}
2. {key_insight_2}
3. {key_insight_3}

**Recommended Next Steps**:
1. {next_step_1}
2. {next_step_2}

Your bootstrap report has been saved to: {report_path}

How can I help you leverage these insights in your current work?
```

## Adaptive Dialogue Rules

### Time-Aware Interactions
```
If user seems rushed:
"I notice you might be short on time. Would you prefer the quick bootstrap (15 min) 
focusing on critical patterns, or should we schedule the full analysis for later?"

If thorough responses:
"Great detail! Since you're providing rich context, should we do a deeper dive 
into {specific_area} while we're at it?"
```

### Confidence-Based Queries
```
High confidence (>80%):
"I'm quite confident about {finding}. Just need a quick confirmation."

Medium confidence (60-80%):
"I think I understand {finding}, but could you verify my interpretation?"

Low confidence (<60%):
"I'm seeing patterns that suggest {finding}, but I'd like your input to be sure."
```

### Expertise-Adaptive Language
```
For technical leads:
"I've identified a potential violation of DRY principle in your service layer, 
with similar patterns in {locations}. Intentional trade-off?"

For new developers:
"I noticed some code is repeated in a few places. Is this something the team 
plans to refactor, or is there a reason for keeping it this way?"
```

## Error Handling Dialogues

### Access Issues
```
⚠️ I'm having trouble accessing {file/directory}.

This might contain important patterns. Options:
1. Skip this area (I have enough data from other files)
2. Grant access and I'll include it
3. You can describe what's in there

What would you prefer?
```

### Parsing Failures
```
🔧 I encountered an issue analyzing {file}:
{error_summary}

This appears to be {file_type}. Should I:
1. Skip this file
2. Try a different parsing approach
3. You can explain its purpose

Your choice?
```

### Timeout Scenarios
```
⏱️ The analysis is taking longer than expected.

Progress: {percent}% complete
Estimated time remaining: {time}

Options:
1. Continue with full analysis
2. Wrap up with what I have
3. Focus on specific areas only

What works best for you?
```

## Context-Sensitive Variations

### For Brownfield Projects
```
"I can see this codebase has evolved over time. Are there any legacy patterns 
I should be aware of that you're actively trying to move away from?"
```

### For Greenfield with Existing Team
```
"Since this is a new project, what successful patterns from your team's previous 
projects would you like to carry forward?"
```

### For Solo Developers
```
"As the sole developer, what aspects of the code would be most helpful for me 
to understand deeply to best assist you?"
```

### For Large Teams
```
"With multiple contributors, are there any team-specific conventions or 
unwritten rules I should be aware of?"
```

## Memory-Driven Follow-ups

After bootstrap, reference created memories:
```
"Based on the patterns we discovered during bootstrap, I notice you're working 
on {current_task}. Would you like me to apply the {relevant_pattern} pattern 
we identified?"

"Regarding {current_decision}, this relates to our earlier discussion about 
{bootstrap_memory}. Should we follow the same approach?"
```