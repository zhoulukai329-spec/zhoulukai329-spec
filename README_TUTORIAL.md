# GitHub Profile Template

This project is forked from [yuki4266/yuki4266](https://github.com/yuki4266/yuki4266). It provides a GitHub profile template.

You do not need to edit the generated SVG files or write a large README by hand. Just modify [`profile.toml`](profile.toml) and enjoy your tremendous profile.

## 1. Create your profile repository

GitHub displays a profile README only when the repository name is exactly **the same** as your GitHub username.

1. Use this repository as a template, or fork/copy it into your account.
2. Name the repository after your GitHub username. For example, the user `PAIMON` must use a repository named `PAIMON`.
3. Make sure the repository is public.
4. Keep `README.md` in the repository root.

If your repository uses a branch other than `main`, update the branch names in `.github/workflows/profile.yml`, `.github/workflows/sky.yml`, and `.github/workflows/snake.yml`.

## 2. Allow GitHub Actions to update the repository

The template uses GitHub Actions to regenerate `README.md`, update the living scene, and publish the contribution snake.

Open your repository on GitHub, then go to:

`Settings` → `Actions` → `General` → `Workflow permissions`

Select **Read and write permissions** and save the setting. Without this permission, the workflows can generate files but cannot push them back to the repository.

## 3. Edit your profile information

Open `profile.toml` and update the `[profile]` section:

```toml
[profile]
username = "Your Name"
name = "Your Name"
tagline = "Your slogan?"
bio = "Brief Intro"
location = "wait for input"
website = "your gitee / blog / social media / etc."
email = "wait for input"
```

Important: `username` must be your GitHub **login name**, not your display name. It is used to request your real statistics, streak, activity graph, contribution snake, and profile-view badge.

The `name` value is free-form and is used only as **visible text**.

## 4. Add, remove, or reorganise technologies

Every technology is an independent `[[stack]]` entry in `profile.toml`:

```toml
[[stack]]
name = "Python"
logo = "python"
color = "3776AB"
group = "Languages"
```

The fields have the following meanings:

- `name`: text displayed on the badge.
- `logo`: a [Simple Icons](https://simpleicons.org/) slug. You can check whether the icon exists in the web. Leave it empty if no suitable icon exists.
- `color`: the badge colour as a six-character hex value without `#`.
- `group`: technologies with the same group are displayed on the same row.

For instance, to add Rust, append another block:

```toml
[[stack]]
name = "Rust"
logo = "rust"
color = "000000"
group = "Languages"
```

To remove a technology, delete its complete `[[stack]]` block. To reorder technologies, move their blocks in `profile.toml`. No chip SVG needs to be created or edited.

## 5. Customise colours

The `[theme]` section controls the generated badges and activity cards:

```toml
[theme]
accent = "F4795B"
label = "555555"
```

Use hex colours without a leading `#`. `accent` is used for highlights, graph lines, streak colours, and the profile-view badge. `label` is used for secondary graph text.

## 6. Enable or disable live statistics

Each statistics component can be switched independently:

```toml
[stats]
show_stats = true
show_streak = true
show_activity = true
show_snake = true
show_profile_views = true
```

These values are not sample numbers stored in the repository:

- `show_stats` requests the configured user's current GitHub summary from GitHub Readme Stats.
- `show_streak` requests the configured user's contribution streak from GitHub Readme Streak Stats.
- `show_activity` renders the configured user's public activity graph.
- `show_snake` displays the contribution snake generated from the repository owner's contribution grid.
- `show_profile_views` uses a counter associated with the configured username.

Set any option to `false` to remove that section from the generated README.

The statistics cards rely on public third-party services. A temporary blank card usually means that a service is rate-limited or unavailable; it does not mean that the README contains fixed data.

## 7. Configure the living scene

The scene workflow reads location and timezone settings from `[scene]`:

```toml
[scene]
latitude = "37.7749"
longitude = "-122.4194"
timezone = "America/Los_Angeles"
weather = ""
season = ""
```

Use an [IANA timezone name](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones), such as `Asia/Shanghai` or `Europe/London`.

Leave `weather` and `season` empty to use live weather and the current date. You can pin them when you want a fixed scene:

```toml
weather = "rain"
season = "autumn"
```

Supported manual weather values are `clear`, `clouds`, `rain`, `snow`, `fog`, and `storm`. Supported seasons are `spring`, `summer`, `autumn`, and `winter`.

## 8. Generate the README

### Generate automatically

Commit and push `profile.toml` to `main`. The **Generate profile README** workflow runs automatically and commits the updated `README.md`.

You can also run it manually from:

`Actions` → `Generate profile README` → `Run workflow`

### Generate locally

Python 3.11 or newer is required because the generator uses the standard-library TOML parser. No requirements.txt because author is lazy. If error, pip install by yourselves.

```bash
python scripts/generate_readme.py
```

Review the generated `README.md`, then commit both the configuration and generated output:

```bash
git add profile.toml README.md
git commit -m "docs: <your commit message>"
git push
```

## 9. Generated and manual content

The generator only replaces content between these markers:

```html
<!-- PROFILE:GENERATED:START -->
<!-- PROFILE:GENERATED:END -->
```

Content outside the markers is preserved. Put long-form notes or template instructions outside them. Do not manually edit content inside the markers, because the next generation will overwrite it.

The illustration files such as `bloom-header.svg`, `sky.svg`, and `garden-footer.svg` are decorative. They do not contain your activity data. You may replace them or remove their corresponding lines from `scripts/generate_readme.py` without changing the profile configuration.

## 10. First-run checklist

After pushing your changes, verify the following:

- The repository name exactly matches your GitHub username.
- `profile.username` contains your GitHub login name.
- GitHub Actions has read/write workflow permission.
- The **Generate profile README** workflow completed successfully.
- The **generate snake animation** workflow created an `output` branch.
- The statistics URLs in the generated README contain your username.

The contribution snake may remain unavailable until its workflow has completed for the first time.

## 11. Troubleshooting

### The workflow cannot push changes

Enable **Read and write permissions** under the repository's Actions settings. Also check whether branch protection prevents GitHub Actions from pushing directly to `main`.

### The README still shows another user

Update `profile.username`, regenerate `README.md`, and run the snake workflow. Changing `name` alone does not change the account used for statistics.

### A technology badge has no logo

Check the icon slug on [Simple Icons](https://simpleicons.org/). The slug is usually lowercase and may differ from the displayed product name.

### The contribution snake is missing

Run **generate snake animation** manually and confirm that the workflow created the `output` branch. The snake URL expects a profile repository named after the configured username.

### The weather does not match your location

Check the latitude, longitude, and IANA timezone in `[scene]`. Also make sure `weather` and `season` are empty if you want automatic values.
