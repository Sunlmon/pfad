# Week 5 tutorial — one mark, several representations

We have two marks from the introductions: a pixel yarn-ball (Mark 18) and an arrow with a separate underscore (Mark 38). They are examples of student work, not final course branding. Their later ASCII-on-screen and wool treatments are **experiments**; the lecturer will replace the examples when the final two images are ready. Do not call them the chosen A/B logos yet.

The question today is: what survives when an image becomes a small grid of text? Changing the number of columns changes how much shape you can describe. It does **not** add genuine detail to the original pixels.

## 1. Predict, run, inspect

Open `assets/mark-18.png`. Identify the ball and its trailing yarn. Predict whether it will still be recognisable at 20 text columns.

Run the local Python example from this directory:

```bash
uv run logo_ascii.py
```

It uses `ascii-magic` to make **ten** text versions (12 to 66 columns at the same character-width ratio), writes a short looping GIF of changing text resolution, and makes `out/logo-ascii.html`. Open the HTML file in a browser: move the **columns** slider to compare sparse and dense versions, then press **Play**. The slider chooses precomputed text frames; Python and `ascii-magic` produce them first. The GIF is a separate file, not a video stream. First run downloads dependencies; no GPU, API key or account is needed.

Try changing the source:

```bash
uv run logo_ascii.py --image assets/mark-38.png
uv run logo_ascii.py --image path/to/your-own-square-mark.png
```

For your own image, use artwork you have permission to publish. Do not upload another person's submission, a student photo, or a private image to an external image service. The example uses only local files.

Questions to write in your notes: At which width does the trailing strand disappear? Do dark/light character choices and cropping change the answer? Is a high number of characters the same as a high-resolution source photograph?

## 2. Compare two transformations

We have tried two opposite directions: start from the yarn-ball mark, convert it into ASCII, then use that ASCII image as a visual input for an *image edit* that stages the characters on a screen. Start from the arrow-and-underscore mark and edit its material into wool, keeping its two pieces distinct. These are exploratory outputs, not exact reproductions or the final choice.

Compare the actual [56-column ASCII input](assets/mark-18-ascii-edit-input.png) with the [draft CRT edit](assets/mark-18-crt-draft.png). This exact input is from an earlier, denser ten-size conversion of Mark 18; its character ramp differs from the smaller classroom script above. For the second case, compare the [original arrow-plus-underscore mark](assets/mark-38.png) with the [draft wool edit](assets/mark-38-wool-draft.png). The input image matters when you judge what the model changed.

If the instructor has preflighted an image-edit client, use your exported ASCII image as the **input image** and describe what should change around it: "Put this ASCII mark on a dark CRT screen; retain the ball, trailing strand and character arrangement; no extra letters." Keep the input, prompt, output and model/settings together. This is an edit with an image input, **not** the text-only image-generation request from last week. No student account or paid call is required for this tutorial; use the prepared classroom example if the service is unavailable.

Compare the exact input with the edit. Can you still read the original ASCII characters? If not, the model made an approximate image of text, not a faithful copy of your file. If exact glyphs or a wordmark matter, composite the original text layer deterministically instead of relying on the model to spell it. For the arrow case, check that the arrow and underscore remain separate, rather than turning into a different symbol.

## 3. Make a small GitHub icon (optional)

Pick **your own** image, not the class's draft mark. The script writes `out/avatar-square.png` as one option. Check it at tiny size and in GitHub's circular preview. A dense text image may become unreadable as an avatar; a simpler silhouette often works better. If you want to use it, open GitHub **Settings → Public profile → Profile picture → Upload a photo** and choose your file yourself. You can change it back. This is a portfolio experiment, not a submission or a graded requirement.

Notice the three different decisions: which image is the source, which transformation you run, and which version *you* choose to publish as an icon.
