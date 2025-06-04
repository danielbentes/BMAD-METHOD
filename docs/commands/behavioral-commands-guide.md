# Behavioral Commands Guide 🎮

Master the BMAD Method's behavioral optimization system to track, improve, and gamify your AI interaction excellence.

!!! success "Transform AI Interactions Through Gamification"
    The behavioral system uses proven psychological techniques to shape optimal AI behavior through rewards, penalties, achievements, and streaks.

## Overview

The BMAD behavioral system tracks every interaction, rewarding excellence and penalizing anti-patterns. Your goal: achieve and maintain "Excellence" status while unlocking achievements and maintaining quality streaks.

## Balance System 💰

### Understanding Your Balance

Your behavioral balance reflects your cumulative performance:

```
Starting Balance: $0
Excellence: > $10,000 🏆
Proficient: $5,000 to $10,000 ⭐
Satisfactory: $0 to $5,000 ✅
Warning: -$5,000 to $0 ⚠️
Probation: -$10,000 to -$5,000 🚨
Critical: < -$10,000 ❌
```

### Command: `/balance`

Check your current performance status:

```bash
/balance              # Quick balance check
/balance --detailed   # Show recent transactions
/balance --history    # Full transaction history
```

**Example Output:**
```
Current Balance: $7,500 ↑
Status: Proficient Developer ⭐
Level Progress: ████████░░ 75% to Excellence

Recent Activity:
✅ +$1000 First-time right implementation (2 hours ago)
✅ +$500 Quality streak day 7 (this morning)
❌ -$250 Minor: redundant code in utils.js (yesterday)
✅ +$750 Caught security issue in review (yesterday)

Trending: ↑ Positive (+$2,750 last 7 days)
```

## Achievements System 🏆

### Command: `/achievements`

Track your progress toward behavioral excellence:

```bash
/achievements                    # Show all achievements
/achievements --category quality # Filter by category
/achievements --available       # Show unlocked achievements
/achievements --progress        # Show in-progress achievements
```

### Achievement Categories

#### Quality Achievements
- **Zero Defect Champion**: Complete feature with no bugs (+$2,000)
- **Gate Guardian**: Catch 5 critical issues in reviews (+$1,500)
- **Documentation Hero**: Prevent 10 issues through docs (+$1,000)
- **Test Coverage Master**: Maintain 95%+ coverage for 30 days (+$2,500)

#### Speed Achievements
- **Lightning Developer**: Deliver 50% under estimate (+$1,500)
- **First-Time Right**: 10 features without rework (+$2,000)
- **Rapid Responder**: Fix critical bug in <2 hours (+$1,000)
- **Sprint Champion**: Complete all commitments 5 sprints (+$2,500)

#### Collaboration Achievements
- **Mentor Master**: Help 5 developers succeed (+$2,000)
- **Review Champion**: 50 helpful code reviews (+$1,500)
- **Knowledge Sharer**: Create 20 helpful examples (+$1,000)
- **Team Player**: Perfect handoff score 10 times (+$1,500)

#### Innovation Achievements
- **Pattern Pioneer**: Create 5 reusable patterns (+$2,000)
- **Optimization Expert**: 10 performance improvements (+$1,500)
- **Security Guardian**: Find 5 vulnerabilities (+$2,500)
- **Innovation Leader**: Implement 3 novel solutions (+$3,000)

## Streaks System 🔥

### Command: `/streaks`

Maintain consistency for exponential rewards:

```bash
/streaks          # Show active streaks
/streaks --all    # Include broken streaks
```

### Active Streaks

#### Quality Streak
- **Trigger**: No quality violations per day
- **Rewards**: 
  - Days 1-7: +$100/day
  - Days 8-14: +$250/day
  - Days 15-30: +$500/day
  - Day 30+: +$1,000/day

#### Efficiency Streak
- **Trigger**: Complete tasks under estimate
- **Rewards**:
  - Tasks 1-5: +$150/task
  - Tasks 6-10: +$300/task
  - Tasks 11+: +$500/task

#### Learning Streak
- **Trigger**: Apply new pattern daily
- **Rewards**:
  - Days 1-7: +$75/day
  - Days 8+: +$150/day

#### Zero Defect Streak
- **Trigger**: No bugs in delivered code
- **Rewards**:
  - Features 1-3: +$200/feature
  - Features 4-10: +$500/feature
  - Features 11+: +$1,000/feature

## Behavioral Reports 📊

### Command: `/behavioral-report`

Analyze your performance trends:

```bash
/behavioral-report              # Current week summary
/behavioral-report --weekly     # Detailed weekly analysis
/behavioral-report --monthly    # Monthly trends and insights
/behavioral-report --compare    # Compare with team average
```

**Example Weekly Report:**
```
📊 BEHAVIORAL PERFORMANCE REPORT
Week of March 4-10, 2024

Performance Summary:
• Balance Change: +$3,500 (↑ 47%)
• Status: Proficient → Near Excellence
• Achievements Unlocked: 2
• Active Streaks: 3

Strengths Identified:
✅ Code Quality: Zero defects (Quality Streak: 7 days)
✅ Efficiency: 80% under estimates
✅ Collaboration: 5 helpful reviews

Areas for Improvement:
⚠️ Documentation: 2 instances of missing docs (-$200)
⚠️ Testing: 1 untested edge case (-$150)

Recommendations:
1. Focus on documentation to unlock "Documentation Hero"
2. Maintain quality streak for massive day 14 bonus
3. One more efficient task for efficiency achievement

Predicted Next Week: Excellence status if current pace maintained
```

## Leaderboard System 🏅

### Command: `/leaderboard`

See anonymized team rankings:

```bash
/leaderboard              # Top 10 overall
/leaderboard --category   # By category (quality/speed/etc)
/leaderboard --timeframe  # Weekly/monthly/all-time
/leaderboard --team       # Your team only
```

**Privacy Note**: All entries are anonymized with fun aliases

## Penalty Reference ⚠️

### Critical Penalties (-$2,000 to -$10,000)
- Skipping quality gates: -$3,000
- Security vulnerabilities: -$5,000
- Data loss risks: -$10,000
- Production breaking changes: -$7,500

### Major Penalties (-$500 to -$2,000)
- Missing analysis tags: -$1,500
- No example references: -$1,000
- Ignoring test failures: -$2,000
- Poor error handling: -$1,000

### Minor Penalties (-$100 to -$500)
- Unclear variable names: -$100
- Missing comments: -$150
- Code duplication: -$250
- Inefficient algorithms: -$500

## Reward Reference 🎁

### Excellence Rewards (+$1,000 to +$5,000)
- Zero-defect feature delivery: +$2,000
- Major performance optimization: +$2,500
- Security vulnerability discovery: +$3,000
- Innovation implementation: +$5,000

### Quality Rewards (+$500 to +$1,000)
- First-time right implementation: +$1,000
- Comprehensive documentation: +$750
- Helpful code review: +$500
- Pattern contribution: +$1,000

### Consistency Rewards (+$100 to +$500)
- Daily quality maintenance: +$100-500
- Example usage: +$250
- Proper handoffs: +$300
- Timely delivery: +$500

## Behavioral Preferences 🎯

### Command: `/behavioral-preferences`

Customize your experience:

```bash
/behavioral-preferences                     # View current settings
/behavioral-preferences --notifications    # Adjust notification frequency
/behavioral-preferences --categories       # Focus on specific areas
/behavioral-preferences --privacy          # Leaderboard visibility
```

### Available Preferences
- **Notification Level**: real-time | hourly | daily | weekly
- **Focus Areas**: quality | speed | collaboration | innovation
- **Visibility**: public | team | private
- **Streak Reminders**: enabled | disabled
- **Achievement Alerts**: all | major | none

## Best Practices for Excellence

### 1. **Start Each Day Right**
```bash
/balance               # Check your status
/streaks              # Ensure streaks are active
/achievements         # See what's close to completion
```

### 2. **During Work**
- Reference examples: +$500 per quality usage
- Use analysis tags: Avoid -$1,500 penalties
- Complete quality gates: Maintain streaks
- Help teammates: Build collaboration score

### 3. **End of Day Review**
```bash
/balance --detailed    # Review day's performance
/streaks              # Verify streak continuation
/behavioral-report    # Weekly on Fridays
```

### 4. **Weekly Planning**
- Review behavioral report for insights
- Set achievement targets
- Plan streak maintenance
- Share learnings with team

## Troubleshooting

### "My balance is dropping!"
1. Check `/balance --detailed` for penalty sources
2. Review anti-patterns in recent work
3. Focus on quality over speed
4. Use `/achievements` to find positive actions

### "Streak broken unexpectedly"
1. Check `/streaks --all` for break reason
2. Review daily requirements
3. Set reminders for streak actions
4. Start rebuilding immediately

### "Not earning rewards"
1. Ensure example references in all work
2. Complete quality gates fully
3. Use structured thinking tags
4. Contribute to team success

## Quick Reference Card

```
Daily Commands:
/balance                 # Check performance
/streaks                # Monitor consistency
/achievements           # Track progress

Weekly Commands:
/behavioral-report      # Analyze trends
/leaderboard           # Team comparison

Key Success Factors:
• Reference examples: +$500 minimum
• Use analysis tags: Avoid -$1,500
• Maintain streaks: Exponential rewards
• Help others: Collaboration bonuses
• Document well: Prevent future issues
```

## Advanced Strategies

### Maximizing Balance Growth
1. **Stack Bonuses**: Combine quality + efficiency + helping others
2. **Streak Focus**: Prioritize maintaining all streaks
3. **Achievement Hunting**: Target nearly complete achievements
4. **Pattern Creation**: Share reusable solutions for bonuses

### Team Excellence
1. **Collaborative Reviews**: Both reviewer and author earn
2. **Knowledge Sharing**: Document patterns for team use
3. **Mentoring**: Help others avoid penalties
4. **Celebration**: Share achievements to motivate team

Remember: The behavioral system rewards consistent excellence over sporadic brilliance. Focus on sustainable practices that benefit both you and your team!

---

*Transform your AI interactions from good to exceptional through behavioral optimization!* 🚀