# README.md

## Installation

Imports required:
- geocoder (`pip install geocoder`)
- numpy (`pip install numpy`)

## Running
- Run `python score_ip.py`
	- Within `score_ip.py`, the default location for the file containing IP information is `ip.txt`, but this can be changed
	- Default test ip is `1.1.1.1` but that also can be changed

## Followup Questions

### False Positives, False Negatives
The issue with our current scoring method is that it only considers the single closest point. Essentially, this is k-nearest neighbors, with k set to 1.

Suppose the nearest point to our testing point was marked FRAUD, but the five next closest points were all marked LOGIN. Our algorithm would place heavy emphasis on the one FRAUD point, whereas it may be likely that the test point is actually not fraudulent. The opposite is also true (if the closest point was LOGIN but the next few were all FRAUD).

Additionally, consider the following example (where we are using a standard Cartesian grid, as opposed to latitudes and longitudes):

FRAUD (3, 4)
LOGIN (6, 8)

Here, if our test point is (0, 0), the "score" to both the fraudulent and non-fraudulent points are both 10. This raises the issue that it's hard to distinguish what the implication of a score is, based off of just one number.

### Distance Calculations
I used the [Haversine distance formula](https://en.wikipedia.org/wiki/Haversine_formula) in calculating the distance between two points. The main issue with this is that it assumes the Earth is spherical, but instead it's slightly ellipsoidal. This leads to some error - on the order of 0.5%, but error nonetheless.

## Further Considerations

Didn't face too many issues with this, I thought it was relatively straightforward.

Potential ideas for improvement:
- Provide a test case (an example data file, test point, and range of values for the output score)
- Allow us to consider some k nearest points, as opposed to just the closest
	- For example, our score could be the mean distance between our test point and the k closest points
	- If more of the k closest points are marked FRAUD than LOGIN, multiply this score by 2