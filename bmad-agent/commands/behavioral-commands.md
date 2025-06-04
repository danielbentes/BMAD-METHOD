# Behavioral Shaping Commands

## User-Facing Commands

### /balance
**Description**: Check your current behavioral balance and status
**Usage**: `/balance [--detailed] [--history]`
**Example Output**:
```
Current Balance: $7,500 ↑
Status: Proficient Developer
Level Progress: ████████░░ 75% to Expert

Recent Activity:
✅ +$1000 First-time right implementation
✅ +$500 Quality streak day 7
❌ -$250 Redundant code in utils.js

Next Achievement: Zero Defect Champion (80% complete)
```

### /achievements
**Description**: View unlocked achievements and progress toward new ones
**Usage**: `/achievements [--category] [--available]`
**Categories**: quality, speed, collaboration, innovation
**Example Output**:
```
🏆 Unlocked Achievements:
✨ Quality Champion - Zero defects for 5 features
⚡ Speed Demon - 50% under estimate
🎓 Mentor - Helped 3 developers succeed

📊 In Progress:
🛡️ Security Guardian (60%) - Find 2 more vulnerabilities
🎯 Sharpshooter (80%) - 2 more first-time-right tasks
```

### /streaks
**Description**: Display active streaks and their status
**Usage**: `/streaks [--all]`
**Example Output**:
```
🔥 Active Streaks:
Quality Streak: 7 days (Next reward at 14 days: +$3000)
Efficiency Streak: 3 tasks (Next reward at 5 tasks: +$750)
Learning Streak: BROKEN - Reset after pattern violation

💡 Tip: Maintain quality streak for massive bonuses!
```

### /leaderboard
**Description**: View anonymized team rankings
**Usage**: `/leaderboard [--timeframe]`
**Timeframes**: daily, weekly, monthly, all-time
**Example Output**:
```
📊 Weekly Leaderboard (Anonymous):
1. Developer A: $15,000 (Master)
2. Developer B: $12,500 (Expert) ← You
3. Developer C: $8,000 (Journeyman)
4. Developer D: $3,500 (Apprentice)
5. Developer E: -$2,000 (Warning)

Your Rank: 2nd of 12 developers
```

### /behavioral-report
**Description**: Generate detailed behavioral analytics report
**Usage**: `/behavioral-report [--period] [--focus]`
**Periods**: day, week, month, quarter
**Focus**: violations, rewards, patterns, improvement
**Example Output**:
```
📈 Weekly Behavioral Report

Balance Change: +$8,500 (↑ 340%)
Violations: 2 minor, 0 major
Rewards: 12 earned
Best Day: Tuesday (+$3,500)

Key Insights:
• Morning coding sessions 3x cleaner
• Test coverage improved 40%
• Collaboration rewards increased

Recommendations:
• Avoid complex tasks after 5 PM
• Continue morning productivity pattern
• Share your testing approach with team
```

## System Commands (Automated)

### apply_violation_penalty
**Trigger**: Automatic on anti-pattern detection
**Action**: 
1. Deduct penalty amount
2. Display violation feedback
3. Reset relevant streaks
4. Log for pattern analysis
5. Suggest correction

### award_achievement_bonus
**Trigger**: Achievement criteria met
**Action**:
1. Add reward amount
2. Display celebration message
3. Update achievement gallery
4. Notify team (if applicable)
5. Store in memory

### streak_check
**Trigger**: After each relevant action
**Action**:
1. Update streak counters
2. Check for reward thresholds
3. Apply streak bonuses
4. Display progress notifications

### behavioral_nudge
**Trigger**: Pre-violation detection
**Action**:
1. Display warning message
2. Suggest alternative approach
3. Reference past success
4. Prevent potential violation

## Administrative Commands

### /reset-balance
**Permission**: Admin only
**Description**: Reset a user's balance
**Usage**: `/reset-balance [user] [amount] --reason`
**Audit**: All resets logged with justification

### /grant-achievement
**Permission**: Admin only
**Description**: Manually grant an achievement
**Usage**: `/grant-achievement [user] [achievement] --reason`
**Use Cases**: Recognition, special circumstances

### /behavioral-analytics
**Permission**: Admin only
**Description**: System-wide behavioral analytics
**Usage**: `/behavioral-analytics [--metric] [--export]`
**Metrics**: violation-trends, reward-distribution, streak-analysis

## Integration Commands

### /sync-behavioral-state
**Description**: Sync behavioral data with memory system
**Automatic**: Every session end
**Manual**: `/sync-behavioral-state [--force]`

### /behavioral-preferences
**Description**: Set personal behavioral tracking preferences
**Options**:
- Notification frequency
- Public/private achievements
- Leaderboard participation
- Nudge sensitivity

**Usage**: `/behavioral-preferences [--set key=value]`

## Quick Reference Card

```
Essential Commands:
/balance          - Check your balance
/achievements     - View achievements  
/streaks         - See active streaks
/leaderboard     - Team rankings

Detailed Analysis:
/behavioral-report [period]  - Full analytics
/behavioral-report week --focus=patterns

Settings:
/behavioral-preferences --set notifications=minimal
/behavioral-preferences --set leaderboard=opt-out
```

## Command Aliases

For convenience, these shorter aliases are available:
- `/bal` → `/balance`
- `/ach` → `/achievements`
- `/str` → `/streaks`
- `/lead` → `/leaderboard`
- `/behav` → `/behavioral-report`

Remember: These commands are tools for self-improvement, not judgment. Use them to understand your patterns, celebrate successes, and identify growth opportunities.