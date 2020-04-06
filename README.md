# Annotation

The complete description of the annotation workflow can be found [here](https://docs.google.com/document/d/1I3Xa67EOMOGoaBJnjxlZcuyEFHYq21gwS4r59t_Mw5g/edit?usp=sharing), and an updated version [here] (https://docs.google.com/document/d/18oJvXGxrzwsVpcJ89DTDtydUihF9I1cPO82G9eexBVA/edit). Steps below only explain the process of selection of a text for annotation.

1. Open the [priority list](https://github.com/OpenITI/Annotation/blob/master/priority_list.csv). It is organized chronologically and is searcheable (the field with a magnifying glass, saying `Search this file`).
1. Texts with `priority` are the ones that should be annotated. Work in chronological order. Texts up to 1000 AH are of top priority.
1. While the priority list will be updated regularly, you should check if a text is not being annotated. To do so, go to [issues](https://github.com/OpenITI/Annotation/issues) and, in the Field **FILTER**, search for the URI of the book that you want to annotate (use either complete URI, like `0597IbnJawzi.Muntazam`, or Author's URI `0597IbnJawzi`, or the title of the book like `Muntazam`; **note:** if you search for `IbnJawzi` nothing will be found).
1. Check results in both `open` and `closed` issues. If nothing found, you can start working on the selected text. (`git fork` > `git clone` > `annotate`).
1. Before you proceed, open an issue ([issues](https://github.com/OpenITI/Annotation/issues) > `New Issue`), using **IN PROGRESS** template.
1. After you finish annotating, send a pull request, close your **IN PROGRESS ISSUE**, and open another issue using **Submission report (for Pull Requests)** template.

# A note for the project curators

You can create an `URGENT` issue to assignn specific text to a specific person. Go to `ISSUES` > `New Issue` > select `URGENT` template > Follow the instructions in the template. 

# Used IDs

## IDs for Collections

| ID | FULL NAME OF A COLLECTION |
|:---|:---|
| JK | *al-Jāmiʿ al-kabīr* |
| Sham30K | *al-Maktabaŧ al-Šāmilaŧ*, official version + additional texts, downloaded from https://archive.org/details/SHAMELH30-1-20 |
| Shamela | *al-Maktabaŧ al-Šāmilaŧ*, www.shamela.ws |
| Shia | http://shiaonlinelibrary.com |
| Yatim | (texts for which we do not have text files yet) |
| Hindawi | https://www.hindawi.org/books/ |


## IDs for Individual Contributions

| IDs | FULL NAME OF AN INDIVIDUAL |
|:----|:---------------------------|
| LMN | Lorenz Matthias Nigst, KITAB |
| GVDB | Gowaart Van Den Bossche, KITAB |
| Khismatulin | Alexei Khismatulin, IOM RAS, St.Peterburg |
| MGR | Maxim Romanov, Vienna / KITAB  |
| SBS | Sarah Bowen Savant, KITAB |

