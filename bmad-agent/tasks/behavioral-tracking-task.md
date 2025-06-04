# Behavioral Tracking Task

## Purpose
Monitor, track, and report on behavioral patterns using the gamification system. This task maintains the reward/penalty balance, tracks achievements, identifies patterns, and provides behavioral insights to shape optimal development practices.

## Execution Protocol

### Phase 1: Session Initialization
1. **Load Current State**
   ```yaml
   behavioral_state:
     current_balance: $0  # or restored from memory
     active_streaks:
       quality_streak: 0
       efficiency_streak: 0
       learning_streak: 0
     session_violations: []
     session_rewards: []
     achievement_progress: {}
   ```

2. **Set Session Goals**
   - Review past performance
   - Identify improvement areas
   - Set achievable targets
   - Display motivational message

### Phase 2: Real-Time Monitoring
Track all actions and apply consequences immediately:

1. **Violation Detection**
   ```python
   def detect_violation(action, context):
       violation = match_against_patterns(action)
       if violation:
           penalty = calculate_penalty(violation, context)
           apply_penalty(penalty)
           provide_feedback(violation, penalty)
           update_streaks(reset=True)
           log_for_learning(violation, context)
   ```

2. **Achievement Recognition**
   ```python
   def check_achievements(action, result):
       for achievement in ACHIEVEMENT_DEFINITIONS:
           if achievement.criteria_met(action, result):
               reward = achievement.reward_amount
               apply_reward(reward)
               celebrate_achievement(achievement)
               update_progress_tracking()
   ```

3. **Streak Management**
   ```yaml
   streak_tracking:
     quality_streak:
       check_after: each_commit
       reset_on: any_violation
       rewards_at: [3, 7, 14, 30]
       
     efficiency_streak:
       check_after: task_completion
       reset_on: missed_deadline
       rewards_at: [5, 10, 25]
       
     learning_streak:
       check_after: pattern_application
       reset_on: pattern_violation
       rewards_at: [3, 5, 10]
   ```

### Phase 3: Behavioral Analysis
Identify patterns and provide insights:

1. **Pattern Detection**
   ```yaml
   behavioral_patterns:
     time_based:
       - morning_performance
       - post_lunch_dip
       - end_of_day_quality
       
     context_based:
       - debugging_efficiency
       - feature_development_quality
       - refactoring_success
       
     emotional_based:
       - post_success_momentum
       - post_failure_recovery
       - pressure_response
   ```

2. **Predictive Warnings**
   ```yaml
   warning_system:
     high_risk_detection:
       - pattern: "3 PM + complex task"
         warning: "Consider a break - violation risk high"
         
       - pattern: "Rushing + no tests"
         warning: "STOP! Tests prevent disasters"
         
       - pattern: "Tired + security code"
         warning: "Security requires full attention"
   ```

### Phase 4: Reporting and Feedback

1. **Real-Time Dashboard**
   ```
   ┌─────────────────────────────────────┐
   │ Current Balance: $7,500 ↑           │
   │ Status: Proficient Developer        │
   │                                     │
   │ Streaks:                           │
   │ 🔥 Quality: 7 days                 │
   │ ⚡ Efficiency: 3 tasks             │
   │ 🧠 Learning: 2 patterns            │
   │                                     │
   │ Today: +$2,000 (2 rewards, 0 violations)│
   │ Next Achievement: Zero Defect (80%) │
   └─────────────────────────────────────┘
   ```

2. **Session Summary**
   ```yaml
   session_report:
     duration: "4 hours"
     starting_balance: $5,500
     ending_balance: $7,500
     net_change: +$2,000
     
     highlights:
       - "Completed task 50% under estimate"
       - "Achieved 100% test coverage"
       - "Extended quality streak to 7 days"
       
     violations: none
     
     recommendations:
       - "You're on fire! Keep the quality streak going"
       - "Consider tackling that complex refactoring"
       - "Share your success patterns with the team"
   ```

## Behavioral Shaping Strategies

### 1. Positive Reinforcement Schedule
```yaml
reinforcement_timing:
  immediate:
    - code_quality_bonus
    - efficiency_reward
    - helping_others_bonus
    
  delayed:
    - streak_rewards
    - level_progression
    - monthly_bonuses
    
  variable:
    - random_excellence_bonus
    - surprise_achievements
    - peer_recognition
```

### 2. Nudge Techniques
```yaml
behavioral_nudges:
  pre_violation:
    - "💡 Remember to add tests!"
    - "🔍 Have you checked for hardcoded values?"
    - "📝 Documentation makes future-you happy"
    
  positive_momentum:
    - "🔥 You're on a roll! Keep it up!"
    - "💪 One more clean commit for a streak bonus!"
    - "🎯 You're 80% toward an achievement!"
    
  recovery_support:
    - "💙 Everyone makes mistakes. Learn and move on."
    - "🌟 Your next success is just around the corner"
    - "📈 You've recovered from worse - you got this!"
```

### 3. Social Dynamics
```yaml
social_features:
  team_leaderboard:
    display: "Anonymous rankings by balance"
    update: "Weekly"
    recognition: "Top performer badge"
    
  peer_recognition:
    mechanism: "Nominate for bonus"
    reward: "+$500 for recognized help"
    visibility: "Team celebration"
    
  mentorship_tracking:
    mentor_bonus: "+$1000 per success"
    mentee_progress: "Shared achievement"
    legacy_building: "Permanent recognition"
```

## Memory Integration

### What to Remember
```yaml
memory_storage:
  behavioral_data:
    - violation_patterns
    - success_patterns
    - optimal_times
    - trigger_contexts
    
  achievement_history:
    - unlocked_achievements
    - near_misses
    - progression_timeline
    
  learning_insights:
    - what_motivates_user
    - what_triggers_violations
    - improvement_trajectory
```

### Learning Application
```yaml
apply_learning:
  personalized_nudges:
    based_on: "Past success patterns"
    timing: "Before high-risk actions"
    
  adaptive_rewards:
    based_on: "What motivates individual"
    adjustment: "Increase effective rewards"
    
  preventive_warnings:
    based_on: "Past violation contexts"
    delivery: "Just-in-time intervention"
```

## Success Metrics

### Individual Progress
- Balance growth rate
- Streak length trends
- Violation frequency reduction
- Achievement velocity

### System Effectiveness
- User engagement level
- Behavior change persistence
- Quality improvement metrics
- Team culture impact

## Integration Points

### With Quality Enforcement
- Automatic penalty application
- Quality gate bonuses
- Brotherhood review rewards

### With Context System
- Context-aware penalty adjustments
- Situation-specific bonuses
- Adaptive behavioral nudges

### With Anti-Pattern System
- Pattern violation penalties
- Learning reinforcement
- Repeat offense escalation

## Gamification Commands

### User Commands
- `/balance` - Check current balance and status
- `/achievements` - View unlocked and available achievements
- `/streaks` - Display active streaks and progress
- `/leaderboard` - See anonymized team rankings
- `/progress` - Detailed behavioral analytics

### System Commands
- `/apply-penalty [amount] [reason]` - Manual penalty
- `/award-bonus [amount] [reason]` - Manual reward
- `/reset-streaks` - Clear all streaks (admin only)
- `/behavioral-report [period]` - Generate report

Remember: The goal is not to punish but to create an environment where quality feels rewarding and violations feel naturally wrong. Every interaction shapes future behavior—make each one count toward building excellence.