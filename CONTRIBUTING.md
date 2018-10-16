# Contributing

## Popular contributions

The most popular way to contribute is adding [new quotes](https://github.com/mubaris/motivate/issues/3). You do it by adding next JSON file in `motivate/data/` directory. The rule is (at least) 20 quotes per file.

### JSON file

The JSON file must have the following structure:

```json
{
	"data": [
		{
			"quote": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
			"author": "Someone"
		},
		{
			"quote": "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris.",
			"author": "Someone else"
		},
		{
			"quote": "Duis aute irure dolor in reprehenderit in voluptate velit.",
			"author": "Unknown"
		},
		{
			"quote": "Excepteur sint occaecat cupidatat non proident.",
			"author": "Someone different"
		}
	]
}
```

> Before you submit your new JSON file, it is helpful to validate your file at [jsonlint.com](https://jsonlint.com/) to make sure it is formatly correct.

## Other contributions

But any improvements are welcome - just open a Pull Request with some description.

## Pull Request

After making your changes, push it to your fork and [submit a Pull Request](https://github.com/mubaris/motivate/compare).

## Discussion

You're also welcome to discuss the idea on [Gitter Chat](https://gitter.im/pymotivate/Lobby?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge).
