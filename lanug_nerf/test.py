from nerfstudio.model_components.renderers import AccumulationRenderer, DepthRenderer, NormalsRenderer, RGBRenderer

from nerfstudio.utils import colormaps, colors, misc
# renderer_rgb = RGBRenderer(background_color=self.config.background_color)
renderer_rgb = RGBRenderer(background_color="last_sample")
print(dir(render_rgb))