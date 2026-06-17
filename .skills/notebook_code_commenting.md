# Notebook Code and Comment Formatting

Use these instructions when AI helps revise assignment notebooks in this repository.

## Notebook Feedback Edits

- Keep tutoring feedback in markdown cells, not as long code comments.
- Place feedback directly before or after the cell it explains.
- Use the orange callout style already used in `wild_suggestions_*.ipynb` files for tutoring notes.
- Keep examples short and focused on the specific concept being taught.

## Code Style

- Prefer beginner-friendly Python syntax appropriate for an intro programming course.
- Avoid advanced fallback logic unless the assignment explicitly calls for it.
- Store repeated values, such as paths and filenames, in variables near the top of the notebook.
- Use `os.path.join()` when building paths from folder names and file names.
- Print important setup values, such as path and filename variables, after defining them so students can verify them in the notebook cell output.
- After reading a file, print a concise confirmation that includes which file was loaded and how many records or values were read.
- When printing a value from data that includes a unique identifier, print the identifier and the value together so the output can be traced back to the source record.
- Use `json.dumps(..., indent=2)` when printing nested dictionaries or lists that would otherwise be hard to read on one line.
- When a cell only defines a function, add a top comment that identifies it as a function cell and print a short confirmation after the function definition.
- In test cells that return multiple records, print output in this order when practical: summary counts, a human-readable table or compact view, then the full nested output with `json.dumps(..., indent=2)`.
- For interactive input or prompt workflows, make the prompt text specific, include an example of valid input when helpful, and make each output message identify the selected record or value.
- For cells that download images or other files, define the output folder and naming pattern clearly, then print the generated file name and full path for each downloaded file.
- Treat this output as practical logging: it should help with real-world testing, troubleshooting, and understanding what happened during a cell run.

## Comment Style

- Comments should clarify what the code does or why the code is needed.
- Do not write code comments in first person.
- Avoid comments such as:

```python
# I add the Data folder to the path so Python can find the vincenty module
```

- Prefer direct, descriptive comments:

```python
# Add the Data folder to the path so Python can find the vincenty module
```

- Avoid comments that simply restate obvious code.
- Add comments when they explain intent, data structure, path setup, or a non-obvious step.

## File and Path Style

- Keep course data files in `assignments/Data`.
- Keep downloaded images in a dedicated image folder, such as `assignments/Data/images`.
- Use clean filenames without duplicate-download suffixes such as `(1)`.
- Prefer names like `Unit08_umich_buildings.json` instead of `Unit08_umich_buildings (1).json`.
- If a filename changes, update the filename variable once and let path variables inherit the change.
- When creating path variables, include a short print check:

```python
print("data_dir:", data_dir)
print("buildings_path:", buildings_path)
```

## File Loading Confirmation

- When a notebook reads a file, include a short output statement so the student can confirm the read worked.
- The message should identify the variable or function loaded, the file path used, and the number of records or values loaded.
- When helpful, print a small preview of the contents, such as the first row or first dictionary, so the student can see the data structure.

```python
print("Setup complete.")
print("Loaded latLngDistanceMeters from", vincenty_path)
print("Loaded", len(umich_buildings), "building records from", buildings_path)
print("Loaded", len(baby_names), "baby name records from", baby_names_path)
```

## Printing Record Values

- When nested data includes an `id` or other unique identifier, include that identifier in the printed output with the selected value.
- Label the output so the reader knows what each value represents.

```python
print("Message id:", first_message_id)
print("Message:", first_message)
```

## Readable Nested Output

- Use `json.dumps()` to format nested dictionaries and lists when the goal is to inspect or log their structure.
- `json.dumps(value, indent=2)` is especially helpful for notebook output because it adds line breaks and indentation.
- Use this for JSON-like data, API responses, nested records, and lists of dictionaries.
- Do not use it when a simple scalar value, such as one name or one number, is enough.
- For test cells that return multiple records, use a three-part output pattern:
  1. Print summary counts, such as requested, returned, skipped, or not found.
  2. Print a human-readable table or compact selected-field view.
  3. Print the full nested data with `json.dumps(..., indent=2)` for debugging.
- This order gives the reader a quick status check, a readable result, and the complete structure for troubleshooting.
- Emphasize that these outputs are not just decorative. Summary counts, readable tables, and structured dumps are practical real-world logging tools that show what activity occurred, what data was returned, and where a problem may have happened.

```python
print(json.dumps(entry["places"], indent=2))
```

```python
print("Movie lookup summary")
print("Titles requested:", len(movie_titles))
print("Movies returned:", len(movies_data))
print("Titles skipped or not found:", len(movie_titles) - len(movies_data))
print()

print("Returned movie title/year summary:")
for movie in movies_data:
    print(movie["Title"], movie["Year"])
print()

print("Returned movie records:")
print(json.dumps(movies_data, indent=2))
```

```python
print("Sorted movie lookup summary")
print("Titles requested:", len(movie_titles))
print("Movies returned:", len(result))
print("Titles skipped or not found:", len(movie_titles) - len(result))
print()

print("     {0:30} {1:4} {2:4}".format("Movie", "Year", "Rating"))
print("     {0:30} {1:4} {2:4}".format("-----", "----", "------"))
for movie in result:
    print("     {0:30} {1:4}   {2:4}".format(movie["Title"], movie["Year"], movie["imdbRating"]))
print()

print("Sorted movie records:")
print(json.dumps(result, indent=2))
```

## Function-Only Cells

- If a notebook cell only defines a function, add a top comment explaining that the cell defines a reusable function for later cells.
- Function-only cells should still have a short output message after the function definition so the student can confirm the cell ran.
- Keep the confirmation separate from the function body.
- Reusable functions should usually return values rather than print large outputs inside the function body.
- Put detailed output, such as `json.dumps(...)`, in the calling or test cell so later cells can control the order and format of their own output.
- Watch for function side effects: if one function prints data while another function calls it inside a loop, that output may appear before the summary or table in the calling cell.

```python
# Function cell: define getOMDBData so it can be called from later cells
def getOMDBData(title):
    ...

print("Function getOMDBData loaded. Call getOMDBData(title) in another cell.")
```

## Downloading Images and Files

- When a notebook downloads images or files, review whether each downloaded item gets a unique output file name.
- Avoid writing multiple records to the same path inside a loop unless overwriting is intentional and explained.
- Define the output folder once near the setup area, such as `images_dir = os.path.join(data_dir, "images")`.
- Build file names from meaningful record values, such as title, year, id, category, or content rating.
- Explain the naming pattern in the feedback cell so the student understands how each file can be traced back to the source record.
- When the file is created from a structured response, such as JSON from an API, use values from that structure to name the file.
- File names should provide context about the content. Avoid generic names such as `poster.jpg` when the file represents a specific record.
- Explain that descriptive file names support accessibility, organization, and troubleshooting because the file name helps identify the content without opening the file.
- In feedback, point out that a meaningful file name can make it easier to find a missing file, detect an overwrite, or connect an image back to the source record.
- Normalize generated file names so they are easier to use later. For intro-level notebooks, simple steps such as `lower()` and `replace(" ", "_")` are usually enough.
- Print the generated file name and full path before or after writing each file.
- Track and print counts for downloaded, skipped or not found, and failed files.
- If the code uses a shared variable such as `poster_path`, check whether it is a fixed setup path or a per-record path created inside the loop.

```python
movies = ["The Shawshank Redemption", "Gladiator", "asdfasdfasdfasdfasdf", "Source Code"]

print("Poster download summary")
print("Movies requested:", len(movies))
print("Poster output folder:", images_dir)
print()

posters_downloaded = 0
movies_skipped = 0
posters_failed = 0

for movie in movies:
    data = getOMDBData(movie)
    if data is False:
        movies_skipped = movies_skipped + 1
        print("Skipped movie, no OMDB record found:", movie)
        continue

    title = data["Title"]
    year = data["Year"]
    rated = data["Rated"]
    link = data["Poster"]

    clean_title = title.lower().replace(" ", "_")
    poster_filename = "{}_{}_{}.jpg".format(clean_title, year, rated.lower())
    poster_path = os.path.join(images_dir, poster_filename)

    print("Poster link for {}: {}".format(title, link))
    print("Poster file name:", poster_filename)
    print("Poster path:", poster_path)

    try:
        poster = requests.get(link)
        f = open(poster_path, "wb")
        f.write(poster.content)
        f.close()
        posters_downloaded = posters_downloaded + 1
        print("Saved poster for {} to {}".format(title, poster_path))
    except:
        posters_failed = posters_failed + 1
        print("Could not retrieve poster for", title)

print("Poster download complete.")
print("Posters downloaded:", posters_downloaded)
print("Movies skipped or not found:", movies_skipped)
print("Poster downloads failed:", posters_failed)
```

## Interactive Prompt Workflows

- When a cell asks the user for input, review the full workflow from prompt to output, not only the syntax.
- Prompt text should explain the expected format and include a short example when the input could be ambiguous.
- If the prompt accepts multiple values, print how many values were entered and how many produced usable records.
- Avoid generic follow-up prompts such as `Want to watch this movie?` when the current record is known. Include the selected title or identifier in the prompt.
- Output messages should name the selected record, not only describe the action generically.
- When the workflow filters out invalid entries, print a count of skipped or not-found values so the student can tell whether the code handled the input as expected.
- For tutoring feedback, point out when the previous output made it hard to know what data was retrieved, selected, skipped, or stored.

```python
# Function cell: define getMovieAdvice so it can be called from later cells
def getMovieAdvice():
    # Ask for movie titles as a comma-separated list
    user_input = input("Enter movie titles separated by commas, for example: Thor, Clue: ")
    # Split the input into individual titles and remove extra spaces
    titles = [t.strip() for t in user_input.split(",")]
    # Retrieve valid movie records sorted by rating
    results = sortedMoviesData(titles)

    print("Movie advice summary")
    print("Titles entered:", len(titles))
    print("Movie records found:", len(results))
    print("Titles skipped or not found:", len(titles) - len(results))

    for movie in results:
        title = movie["Title"]
        if title in viewed_movies:
            print("Already viewed:", title)
        else:
            print("{} ({}) - Rating: {}".format(title, movie["Year"], movie["imdbRating"]))
            answer = input("Want to watch {}? (yes or no): ".format(title))
            if answer.lower() == "yes":
                markAsViewed(title)
                print("Marked as viewed:", title)
                print("Runtime:", movie["Runtime"])

print("Function getMovieAdvice loaded. Call getMovieAdvice() in another cell.")
```
