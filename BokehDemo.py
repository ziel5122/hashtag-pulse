#Code will be significantly simplified in the 0.4 release
import time
from bokeh.models.renderers import GlyphRenderer
import bokeh
import bokeh.models.renderers

renderer = [r for r in bokeh.models.renderers if isinstance(r, GlyphRenderer)][0]
ds = renderer.data_source
x = 0
y = 0
while True:
    ds.data["x"] = x
    ds.data["y"] = y
    ds._dirty = True
    session().store_obj(ds)
    time.sleep(1.5)
    i+=1
    x += 1
    y += 1
