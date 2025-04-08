import basilisk as bsk

engine = bsk.Engine(title=None)
scene = bsk.Scene(engine)

# Load meshes
sphere_mesh = bsk.Mesh('models/sphere.obj')
monkey_mesh = bsk.Mesh('models/monkey.obj')

# Load images
floor_albedo = bsk.Image('textures/floor_albedo.png')
floor_normal = bsk.Image('textures/floor_normal.png')
mud_albedo   = bsk.Image('textures/mud.png')
mud_normal   = bsk.Image('textures/mud_normal.png')
cloth_albedo = bsk.Image('textures/cloth_albedo.png')
cloth_normal = bsk.Image('textures/cloth_normal.png')
landscape = bsk.Image('textures/landscape.png')

# Load materials
floor     = bsk.Material(texture=floor_albedo, normal=floor_normal, roughness=.25, specular=2, clearcoat=1, anisotropic=.25)
mud       = bsk.Material(texture=mud_albedo, normal=mud_normal, roughness=.5, specular=2, clearcoat=.5)
cloth     = bsk.Material(texture=cloth_albedo, normal=cloth_normal, roughness=.8, specular=1.5, clearcoat=.8, clearcoat_gloss=.6)
emissive  = bsk.Material(emissive_color=(500, 150, 150))
landscape = bsk.Material(texture=landscape)
zach = bsk.Material(texture=bsk.Image('textures/zach.png'))
bear = bsk.Material(texture=bsk.Image('textures/bear.png'))


# Add Nodes
node = bsk.Node(material=bear, rotation=(0, 3.14, 0), scale=(5, 5, 8))
scene.add(node)

# Kuwahara tools
kuwahara_shader = bsk.Shader(engine, 'shader/frame.vert', 'shader/kuwahara.frag')
kuwahara_renderer = bsk.Framebuffer(engine, kuwahara_shader, scale=1)
temp_buffer = bsk.Framebuffer(engine, scale=1)

while engine.running:
    scene.update(render=False)

    scene.render(kuwahara_renderer)
    kuwahara_renderer.render()

    engine.update(render=False)