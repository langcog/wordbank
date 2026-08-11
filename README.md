Wordbank
========

Wordbank is an open database of children's vocabulary development, archiving
data from the MacArthur-Bates Communicative Development Inventories (CDIs)
contributed by researchers around the world.

> [!IMPORTANT]
> **This repository contains the legacy Wordbank site** (Django + MySQL +
> Shiny), which has been replaced by a new static architecture. This code is
> no longer under active development.

The Wordbank ecosystem now lives at:

- **Website** — [langcog.github.io/wordbank-datapage](https://langcog.github.io/wordbank-datapage)
  (soon again at wordbank.stanford.edu): interactive visualizations of
  vocabulary norms, item trajectories, cross-linguistic trajectories,
  semantic networks, CDI scoring, and filtered data downloads. Source:
  [langcog/wordbank-datapage](https://github.com/langcog/wordbank-datapage).
- **Data** — the versioned
  [datapages.wordbank](https://stanford.redivis.com/datasets/627v-9ewzpdvz0)
  dataset on Redivis: every release is a citable snapshot, freely
  downloadable.
- **R package** — [wordbankr](https://github.com/langcog/wordbankr), which
  reads the Redivis dataset directly. See the
  [tutorial vignette](http://langcog.github.io/wordbankr).

If you use Wordbank, please cite:

> Frank, M. C., Braginsky, M., Yurovsky, D., & Marchman, V. A. (2017).
> Wordbank: An open repository for developmental vocabulary data.
> *Journal of Child Language, 44*(3), 677–694.
> [doi:10.1017/S0305000916000209](https://doi.org/10.1017/S0305000916000209)
