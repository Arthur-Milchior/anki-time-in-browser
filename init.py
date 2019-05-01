from aqt.browser import *
from .config import getUserOption
from .consts import *
from anki.lang import _


def columnData(self, index):
        format = getUserOption("Time format", "%Y-%m-%d @ %H:%M")
        row = index.row()
        col = index.column()
        type = self.columnType(col)
        c = self.getCard(index)
        if type == "question":
            return self.question(c)
        elif type == "answer":
            return self.answer(c)
        elif type == "noteFld":
            f = c.note()
            return htmlToTextLine(f.fields[self.col.models.sortIdx(f.model())])
        elif type == "template":
            t = c.template()['name']
            if c.model()['type'] == MODEL_CLOZE:
                t += " %d" % (c.ord+1)
            return t
        elif type == "cardDue":
            # catch invalid dates
            try:
                t = self.nextDue(c, index)
            except:
                t = ""
            if c.queue < 0:
                t = "(" + t + ")"
            return t
        elif type == "noteCrt":
            return time.strftime(format, time.localtime(c.note().id/1000))
        elif type == "noteMod":
            return time.strftime(format, time.localtime(c.note().mod))
        elif type == "cardMod":
            return time.strftime(format, time.localtime(c.mod))
        elif type == "cardReps":
            return str(c.reps)
        elif type == "cardLapses":
            return str(c.lapses)
        elif type == "noteTags":
            return " ".join(c.note().tags)
        elif type == "note":
            return c.model()['name']
        elif type == "cardIvl":
            if c.type == 0:
                return _("(new)")
            elif c.type == 1:
                return _("(learning)")
            return fmtTimeSpan(c.ivl*86400)
        elif type == "cardEase":
            if c.type == 0:
                return _("(new)")
            return "%d%%" % (c.factor/10)
        elif type == "deck":
            if c.odid:
                # in a cram deck
                return "%s (%s)" % (
                    self.browser.mw.col.decks.name(c.did),
                    self.browser.mw.col.decks.name(c.odid))
            # normal deck
            return self.browser.mw.col.decks.name(c.did)

DataModel.columnData = columnData

def nextDue(self, c, index):
        format = getUserOption("Time format", "%Y-%m-%d @ %H:%M")
        if c.odid:
            return _("(filtered)")
        elif c.queue == QUEUE_NEW_CRAM or c.type == CARD_NEW:
            return str(c.due)
        elif c.queue == QUEUE_LRN:
            return time.strftime(format, time.localtime(c.due))
        elif c.queue in (QUEUE_REV, QUEUE_DAY_LRN) or (c.type == CARD_DUE and
                                                          c.queue < 0#suspended or buried
        ):
            date = time.time() + ((c.due - self.col.sched.today)*86400)
            return time.strftime("%Y-%m-%d", time.localtime(date))
        else:
            return ""
DataModel.nextDue = nextDue
