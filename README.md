# Configure Browser's time
## Rationale
The browser (and the [advanced browser](https://ankiweb.net/shared/info/874215009)) both show date but not time. Today, knowing the hour and minute was something I have found useful. Hence this add-on.


## Warning
While this add-on is compatible with the advanced browser, it will only configure the time of standard columns. To change the advanced browser's column, it would have been necessary to edit the other add-on.

## Configuration
There is a single value in the configuration file. It is a parametrization string as explained in https://docs.python.org/2/library/time.html
## Internal
It modifieds the methods:
* Aqt.browser.DataModel.columnData
* Aqt.browser.DataModel.nextDue

## Version 2.0
None

## Links, licence and credits

Key         |Value
------------|-------------------------------------------------------------------
Copyright   | Arthur Milchior <arthur@milchior.fr>
Based on    | Anki code by Damien Elmes <anki@ichi2.net>
License     | GNU AGPL, version 3 or later; http://www.gnu.org/licenses/agpl.html
Source in   | https://github.com/Arthur-Milchior/anki-time-in-browser
Addon number| [1243668133](https://ankiweb.net/shared/info/1243668133)
