[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

# CAP GENERATOR

Code to generate .mpl and .smps files for the instances of stochastic capacitated facility location problem (CAP).
Data files are taken from Bodur et al. [1]. Deterministic model originates from OR-Library [2] and scenarios
were generated by Bodur. First stage is pure binary and the second stage is continuous with complete recourse.

Instances for 5, 50, 250, 1000, 2000, 3000, 4000, 5000 are already generated and
located in [output](https://github.com/pashtetGP/cap_generator/tree/master/output) directory. 
Click [here](https://github.com/pashtetgp/cap_generator/releases/latest/download/instances.zip) to download them all. 

## Instance Characteristics

| Instance    | Stages | Scenarios | 1st Int | 1st Bin | 1st Cont | 1st Constraints | 2nd Int | 2nd Bin | 2nd Cont | 2nd Constraints |
|-------------|--------|-----------|---------|---------|----------|-----------------|---------|---------|----------|-----------------|
| cap101_1000 | 2      | 1000      | 0       | 25      | 0        | 1               | 0       | 0       | 1250     | 75              |
| cap101_2000 | 2      | 2000      | 0       | 25      | 0        | 1               | 0       | 0       | 1250     | 75              |
| cap101_250  | 2      | 250       | 0       | 25      | 0        | 1               | 0       | 0       | 1250     | 75              |
| cap101_3000 | 2      | 3000      | 0       | 25      | 0        | 1               | 0       | 0       | 1250     | 75              |
| cap101_4000 | 2      | 4000      | 0       | 25      | 0        | 1               | 0       | 0       | 1250     | 75              |
| cap101_5    | 2      | 5         | 0       | 25      | 0        | 1               | 0       | 0       | 1250     | 75              |
| cap101_50   | 2      | 50        | 0       | 25      | 0        | 1               | 0       | 0       | 1250     | 75              |
| cap101_5000 | 2      | 5000      | 0       | 25      | 0        | 1               | 0       | 0       | 1250     | 75              |
| cap102_1000 | 2      | 1000      | 0       | 25      | 0        | 1               | 0       | 0       | 1250     | 75              |
| cap102_2000 | 2      | 2000      | 0       | 25      | 0        | 1               | 0       | 0       | 1250     | 75              |
| cap102_250  | 2      | 250       | 0       | 25      | 0        | 1               | 0       | 0       | 1250     | 75              |
| cap102_3000 | 2      | 3000      | 0       | 25      | 0        | 1               | 0       | 0       | 1250     | 75              |
| cap102_4000 | 2      | 4000      | 0       | 25      | 0        | 1               | 0       | 0       | 1250     | 75              |
| cap102_5    | 2      | 5         | 0       | 25      | 0        | 1               | 0       | 0       | 1250     | 75              |
| cap102_50   | 2      | 50        | 0       | 25      | 0        | 1               | 0       | 0       | 1250     | 75              |
| cap102_5000 | 2      | 5000      | 0       | 25      | 0        | 1               | 0       | 0       | 1250     | 75              |
| cap103_1000 | 2      | 1000      | 0       | 25      | 0        | 1               | 0       | 0       | 1250     | 75              |
| cap103_2000 | 2      | 2000      | 0       | 25      | 0        | 1               | 0       | 0       | 1250     | 75              |
| cap103_250  | 2      | 250       | 0       | 25      | 0        | 1               | 0       | 0       | 1250     | 75              |
| cap103_3000 | 2      | 3000      | 0       | 25      | 0        | 1               | 0       | 0       | 1250     | 75              |
| cap103_4000 | 2      | 4000      | 0       | 25      | 0        | 1               | 0       | 0       | 1250     | 75              |
| cap103_5    | 2      | 5         | 0       | 25      | 0        | 1               | 0       | 0       | 1250     | 75              |
| cap103_50   | 2      | 50        | 0       | 25      | 0        | 1               | 0       | 0       | 1250     | 75              |
| cap103_5000 | 2      | 5000      | 0       | 25      | 0        | 1               | 0       | 0       | 1250     | 75              |
| cap111_1000 | 2      | 1000      | 0       | 50      | 0        | 1               | 0       | 0       | 2500     | 100             |
| cap111_2000 | 2      | 2000      | 0       | 50      | 0        | 1               | 0       | 0       | 2500     | 100             |
| cap111_250  | 2      | 250       | 0       | 50      | 0        | 1               | 0       | 0       | 2500     | 100             |
| cap111_3000 | 2      | 3000      | 0       | 50      | 0        | 1               | 0       | 0       | 2500     | 100             |
| cap111_4000 | 2      | 4000      | 0       | 50      | 0        | 1               | 0       | 0       | 2500     | 100             |
| cap111_5    | 2      | 5         | 0       | 50      | 0        | 1               | 0       | 0       | 2500     | 100             |
| cap111_50   | 2      | 50        | 0       | 50      | 0        | 1               | 0       | 0       | 2500     | 100             |
| cap111_5000 | 2      | 5000      | 0       | 50      | 0        | 1               | 0       | 0       | 2500     | 100             |
| cap112_1000 | 2      | 1000      | 0       | 50      | 0        | 1               | 0       | 0       | 2500     | 100             |
| cap112_2000 | 2      | 2000      | 0       | 50      | 0        | 1               | 0       | 0       | 2500     | 100             |
| cap112_250  | 2      | 250       | 0       | 50      | 0        | 1               | 0       | 0       | 2500     | 100             |
| cap112_3000 | 2      | 3000      | 0       | 50      | 0        | 1               | 0       | 0       | 2500     | 100             |
| cap112_4000 | 2      | 4000      | 0       | 50      | 0        | 1               | 0       | 0       | 2500     | 100             |
| cap112_5    | 2      | 5         | 0       | 50      | 0        | 1               | 0       | 0       | 2500     | 100             |
| cap112_50   | 2      | 50        | 0       | 50      | 0        | 1               | 0       | 0       | 2500     | 100             |
| cap112_5000 | 2      | 5000      | 0       | 50      | 0        | 1               | 0       | 0       | 2500     | 100             |
| cap113_1000 | 2      | 1000      | 0       | 50      | 0        | 1               | 0       | 0       | 2500     | 100             |
| cap113_2000 | 2      | 2000      | 0       | 50      | 0        | 1               | 0       | 0       | 2500     | 100             |
| cap113_250  | 2      | 250       | 0       | 50      | 0        | 1               | 0       | 0       | 2500     | 100             |
| cap113_3000 | 2      | 3000      | 0       | 50      | 0        | 1               | 0       | 0       | 2500     | 100             |
| cap113_4000 | 2      | 4000      | 0       | 50      | 0        | 1               | 0       | 0       | 2500     | 100             |
| cap113_5    | 2      | 5         | 0       | 50      | 0        | 1               | 0       | 0       | 2500     | 100             |
| cap113_50   | 2      | 50        | 0       | 50      | 0        | 1               | 0       | 0       | 2500     | 100             |
| cap113_5000 | 2      | 5000      | 0       | 50      | 0        | 1               | 0       | 0       | 2500     | 100             |
| cap114_1000 | 2      | 1000      | 0       | 50      | 0        | 1               | 0       | 0       | 2500     | 100             |
| cap114_2000 | 2      | 2000      | 0       | 50      | 0        | 1               | 0       | 0       | 2500     | 100             |
| cap114_250  | 2      | 250       | 0       | 50      | 0        | 1               | 0       | 0       | 2500     | 100             |
| cap114_3000 | 2      | 3000      | 0       | 50      | 0        | 1               | 0       | 0       | 2500     | 100             |
| cap114_4000 | 2      | 4000      | 0       | 50      | 0        | 1               | 0       | 0       | 2500     | 100             |
| cap114_5    | 2      | 5         | 0       | 50      | 0        | 1               | 0       | 0       | 2500     | 100             |
| cap114_50   | 2      | 50        | 0       | 50      | 0        | 1               | 0       | 0       | 2500     | 100             |
| cap114_5000 | 2      | 5000      | 0       | 50      | 0        | 1               | 0       | 0       | 2500     | 100             |
| cap121_1000 | 2      | 1000      | 0       | 50      | 0        | 1               | 0       | 0       | 2500     | 100             |
| cap121_2000 | 2      | 2000      | 0       | 50      | 0        | 1               | 0       | 0       | 2500     | 100             |
| cap121_250  | 2      | 250       | 0       | 50      | 0        | 1               | 0       | 0       | 2500     | 100             |
| cap121_3000 | 2      | 3000      | 0       | 50      | 0        | 1               | 0       | 0       | 2500     | 100             |
| cap121_4000 | 2      | 4000      | 0       | 50      | 0        | 1               | 0       | 0       | 2500     | 100             |
| cap121_5    | 2      | 5         | 0       | 50      | 0        | 1               | 0       | 0       | 2500     | 100             |
| cap121_50   | 2      | 50        | 0       | 50      | 0        | 1               | 0       | 0       | 2500     | 100             |
| cap121_5000 | 2      | 5000      | 0       | 50      | 0        | 1               | 0       | 0       | 2500     | 100             |
| cap122_1000 | 2      | 1000      | 0       | 50      | 0        | 1               | 0       | 0       | 2500     | 100             |
| cap122_2000 | 2      | 2000      | 0       | 50      | 0        | 1               | 0       | 0       | 2500     | 100             |
| cap122_250  | 2      | 250       | 0       | 50      | 0        | 1               | 0       | 0       | 2500     | 100             |
| cap122_3000 | 2      | 3000      | 0       | 50      | 0        | 1               | 0       | 0       | 2500     | 100             |
| cap122_4000 | 2      | 4000      | 0       | 50      | 0        | 1               | 0       | 0       | 2500     | 100             |
| cap122_5    | 2      | 5         | 0       | 50      | 0        | 1               | 0       | 0       | 2500     | 100             |
| cap122_50   | 2      | 50        | 0       | 50      | 0        | 1               | 0       | 0       | 2500     | 100             |
| cap122_5000 | 2      | 5000      | 0       | 50      | 0        | 1               | 0       | 0       | 2500     | 100             |
| cap123_1000 | 2      | 1000      | 0       | 50      | 0        | 1               | 0       | 0       | 2500     | 100             |
| cap123_2000 | 2      | 2000      | 0       | 50      | 0        | 1               | 0       | 0       | 2500     | 100             |
| cap123_250  | 2      | 250       | 0       | 50      | 0        | 1               | 0       | 0       | 2500     | 100             |
| cap123_3000 | 2      | 3000      | 0       | 50      | 0        | 1               | 0       | 0       | 2500     | 100             |
| cap123_4000 | 2      | 4000      | 0       | 50      | 0        | 1               | 0       | 0       | 2500     | 100             |
| cap123_5    | 2      | 5         | 0       | 50      | 0        | 1               | 0       | 0       | 2500     | 100             |
| cap123_50   | 2      | 50        | 0       | 50      | 0        | 1               | 0       | 0       | 2500     | 100             |
| cap123_5000 | 2      | 5000      | 0       | 50      | 0        | 1               | 0       | 0       | 2500     | 100             |
| cap124_1000 | 2      | 1000      | 0       | 50      | 0        | 1               | 0       | 0       | 2500     | 100             |
| cap124_2000 | 2      | 2000      | 0       | 50      | 0        | 1               | 0       | 0       | 2500     | 100             |
| cap124_250  | 2      | 250       | 0       | 50      | 0        | 1               | 0       | 0       | 2500     | 100             |
| cap124_3000 | 2      | 3000      | 0       | 50      | 0        | 1               | 0       | 0       | 2500     | 100             |
| cap124_4000 | 2      | 4000      | 0       | 50      | 0        | 1               | 0       | 0       | 2500     | 100             |
| cap124_5    | 2      | 5         | 0       | 50      | 0        | 1               | 0       | 0       | 2500     | 100             |
| cap124_50   | 2      | 50        | 0       | 50      | 0        | 1               | 0       | 0       | 2500     | 100             |
| cap124_5000 | 2      | 5000      | 0       | 50      | 0        | 1               | 0       | 0       | 2500     | 100             |
| cap131_1000 | 2      | 1000      | 0       | 50      | 0        | 1               | 0       | 0       | 2500     | 100             |
| cap131_2000 | 2      | 2000      | 0       | 50      | 0        | 1               | 0       | 0       | 2500     | 100             |
| cap131_250  | 2      | 250       | 0       | 50      | 0        | 1               | 0       | 0       | 2500     | 100             |
| cap131_3000 | 2      | 3000      | 0       | 50      | 0        | 1               | 0       | 0       | 2500     | 100             |
| cap131_4000 | 2      | 4000      | 0       | 50      | 0        | 1               | 0       | 0       | 2500     | 100             |
| cap131_5    | 2      | 5         | 0       | 50      | 0        | 1               | 0       | 0       | 2500     | 100             |
| cap131_50   | 2      | 50        | 0       | 50      | 0        | 1               | 0       | 0       | 2500     | 100             |
| cap131_5000 | 2      | 5000      | 0       | 50      | 0        | 1               | 0       | 0       | 2500     | 100             |
| cap132_1000 | 2      | 1000      | 0       | 50      | 0        | 1               | 0       | 0       | 2500     | 100             |
| cap132_2000 | 2      | 2000      | 0       | 50      | 0        | 1               | 0       | 0       | 2500     | 100             |
| cap132_250  | 2      | 250       | 0       | 50      | 0        | 1               | 0       | 0       | 2500     | 100             |
| cap132_3000 | 2      | 3000      | 0       | 50      | 0        | 1               | 0       | 0       | 2500     | 100             |
| cap132_4000 | 2      | 4000      | 0       | 50      | 0        | 1               | 0       | 0       | 2500     | 100             |
| cap132_5    | 2      | 5         | 0       | 50      | 0        | 1               | 0       | 0       | 2500     | 100             |
| cap132_50   | 2      | 50        | 0       | 50      | 0        | 1               | 0       | 0       | 2500     | 100             |
| cap132_5000 | 2      | 5000      | 0       | 50      | 0        | 1               | 0       | 0       | 2500     | 100             |
| cap133_1000 | 2      | 1000      | 0       | 50      | 0        | 1               | 0       | 0       | 2500     | 100             |
| cap133_2000 | 2      | 2000      | 0       | 50      | 0        | 1               | 0       | 0       | 2500     | 100             |
| cap133_250  | 2      | 250       | 0       | 50      | 0        | 1               | 0       | 0       | 2500     | 100             |
| cap133_3000 | 2      | 3000      | 0       | 50      | 0        | 1               | 0       | 0       | 2500     | 100             |
| cap133_4000 | 2      | 4000      | 0       | 50      | 0        | 1               | 0       | 0       | 2500     | 100             |
| cap133_5    | 2      | 5         | 0       | 50      | 0        | 1               | 0       | 0       | 2500     | 100             |
| cap133_50   | 2      | 50        | 0       | 50      | 0        | 1               | 0       | 0       | 2500     | 100             |
| cap133_5000 | 2      | 5000      | 0       | 50      | 0        | 1               | 0       | 0       | 2500     | 100             |
| cap134_1000 | 2      | 1000      | 0       | 50      | 0        | 1               | 0       | 0       | 2500     | 100             |
| cap134_2000 | 2      | 2000      | 0       | 50      | 0        | 1               | 0       | 0       | 2500     | 100             |
| cap134_250  | 2      | 250       | 0       | 50      | 0        | 1               | 0       | 0       | 2500     | 100             |
| cap134_3000 | 2      | 3000      | 0       | 50      | 0        | 1               | 0       | 0       | 2500     | 100             |
| cap134_4000 | 2      | 4000      | 0       | 50      | 0        | 1               | 0       | 0       | 2500     | 100             |
| cap134_5    | 2      | 5         | 0       | 50      | 0        | 1               | 0       | 0       | 2500     | 100             |
| cap134_50   | 2      | 50        | 0       | 50      | 0        | 1               | 0       | 0       | 2500     | 100             |
| cap134_5000 | 2      | 5000      | 0       | 50      | 0        | 1               | 0       | 0       | 2500     | 100             |

[1] Bodur, Merve, Sanjeeb Dash, Oktay Günlük, and James Luedtke. “Strengthened Benders Cuts for Stochastic Integer Programs with Continuous Recourse.” INFORMS Journal on Computing 29, no. 1 (2017): 77–91.

[2] Beasley, J E. “OR-LIBRARY.” Accessed October 29, 2020. http://people.brunel.ac.uk/~mastjjb/jeb/info.html.

# Prerequisites
* python 3.x

<!-- ROADMAP -->
# Roadmap

See the [open issues](https://github.com/pashtetgp/optconvert/issues) for a list of proposed features (and known issues).

<!-- CONTRIBUTING -->
# Contributing

Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<!-- LICENSE -->
# License

Distributed under the MIT License. See `LICENSE` for more information.

<!-- CONTACT -->
# Contact

Pavlo Glushko

Project Link: [https://github.com/pashtetgp/cap_generator](https://github.com/pashtetgp/cap_generator)

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/pashtetgp/optconvert.svg?style=flat-square
[contributors-url]: https://github.com/pashtetgp/optconvert/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/pashtetgp/optconvert.svg?style=flat-square
[forks-url]: https://github.com/pashtetgp/optconvert/network/members
[stars-shield]: https://img.shields.io/github/stars/pashtetgp/optconvert.svg?style=flat-square
[stars-url]: https://github.com/pashtetgp/optconvert/stargazers
[issues-shield]: https://img.shields.io/github/issues/pashtetgp/optconvert.svg?style=flat-square
[issues-url]: https://github.com/pashtetgp/optconvert/issues
[license-shield]: https://img.shields.io/github/license/pashtetgp/optconvert.svg?style=flat-square
[license-url]: https://github.com/pashtetgp/optconvert/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/pavloglushko