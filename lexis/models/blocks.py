from wagtail.core import blocks

# STREAM FIELD CLASSES for RePEATING ARRAYS//////////////////////////////////////
# Create stream for an object array
# class represents a block field inheriits from struck blocks
class Derivations(blocks.TextBlock):
    class Meta:
        template = "lexis/derivations.html"
        icon = "edit"
        label = "Derivations"


class LexisRoot(blocks.TextBlock):
    class Meta:
        template = "lexis/lexis_root.html"
        icon = "edit"
        label = "LexisRoot"


class Highlight(blocks.TextBlock):
    class Meta:
        icon = "edit"
        label = "Highlight"


class Application(blocks.TextBlock):
    class Meta:
        icon = "edit"
        label = "Application"


class Exploration(blocks.TextBlock):
    class Meta:
        icon = "edit"
        label = "Exploration"

