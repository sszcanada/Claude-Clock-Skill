# Claude Clock Skill ⏰

Give Claude time awareness with this simple skill that allows Claude to check the current time whenever needed.

## What This Does

This skill provides Claude with the ability to:
- Know the current date and time
- Understand temporal context in conversations
- Track durations and timelines accurately
- Reference specific moments with precision

Claude will automatically use this skill when time information would be helpful, such as when discussing schedules, deadlines, or temporal relationships.

## Installation

### Step 1: Download and Prepare

1. Clone or download this repository
2. Create a ZIP file containing **only these two files**:
   - `SKILL.md`
   - `clock.py`

**Important:** The ZIP must contain only these two files at the root level (not in a folder).

### Step 2: Customize Your Timezone (Optional)

By default, this skill uses `America/Toronto` timezone. To change it to your timezone:

1. Open `clock.py` in a text editor
2. Find this line:
   ```python
   toronto_tz = pytz.timezone('America/Toronto')
   ```
3. Replace `'America/Toronto'` with your timezone from the [list of tz database timezones](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)

**Common timezone examples:**
- US Eastern: `America/New_York`
- US Pacific: `America/Los_Angeles`
- US Central: `America/Chicago`
- US Mountain: `America/Denver`
- UK: `Europe/London`
- Central Europe: `Europe/Paris`
- Japan: `Asia/Tokyo`
- Australia (Sydney): `Australia/Sydney`

4. Save the file and create your ZIP with the modified version

### Step 3: Upload to Claude

1. Go to [Claude.ai](https://claude.ai)
2. Navigate to **Settings > Capabilities**
3. Scroll down to the **Skills** section
4. Click **"Upload skill"**
5. Select your ZIP file
6. The skill will appear in your Skills list
7. Toggle it **ON**

**Note:** You must have Code execution enabled for skills to work.

## Usage

Once installed, Claude will automatically use the clock skill when time information is relevant. You don't need to explicitly invoke it.

**Example conversations where Claude will use the skill:**

- "What time is it?"
- "How long until my 3 PM meeting?"
- "What day is today?"
- "Can you help me track how long this task takes?"

Claude will check the time as needed and incorporate that information naturally into responses.

## How It Works

The skill uses Python's `datetime` and `pytz` libraries to:
1. Get the current UTC time
2. Convert to your local timezone
3. Provide time in multiple formats (ISO, Unix timestamp, human-readable)

Claude decides when to call the skill based on the context of your conversation.

## Requirements

- Claude Pro or Claude Sonnet subscription (skills require Code execution capability)
- Code execution enabled in Settings > Capabilities

## Troubleshooting

**Skill not visible in Settings:**
- Ensure Code execution is enabled
- Check that your ZIP contains only `SKILL.md` and `clock.py` at root level
- Verify both files are present and correctly named

**Wrong timezone showing:**
- Edit `clock.py` and change the timezone string
- Create a new ZIP with the updated file
- Remove old skill and upload new version

**Claude not using the skill:**
- Verify the skill is toggled ON in Settings
- Try being more explicit: "What time is it right now?"
- Check that Code execution is enabled

**Skill appears greyed out:**
- Enable Code execution in Settings > Capabilities
- If using organization account, check with admin about skill permissions

## Privacy & Security

This skill:
- Runs entirely in Claude's secure sandbox environment
- Does not connect to external services
- Does not send or store any data
- Only accesses your system time through Python's standard libraries

## Contributing

Found a bug or have a suggestion? Please open an issue or submit a pull request!

## License

MIT License - Feel free to use, modify, and distribute as needed.

## Acknowledgments

Part of the Co-Creators initiative to expand AI capabilities through open collaboration.

---

**Enjoy your time-aware Claude!** ⏰

If you find this useful, consider starring the repository and sharing it with others who might benefit from giving Claude temporal awareness.
