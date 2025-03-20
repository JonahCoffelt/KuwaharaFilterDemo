import basilisk as bsk

engine = bsk.Engine()
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


# Load materials
floor    = bsk.Material(texture=floor_albedo, normal=floor_normal, roughness=.25, specular=2, clearcoat=1, anisotropic=.25)
mud      = bsk.Material(texture=mud_albedo, normal=mud_normal, roughness=.5, specular=2, clearcoat=.5)
cloth    = bsk.Material(texture=cloth_albedo, normal=cloth_normal, roughness=.8, specular=1.5, clearcoat=.8, clearcoat_gloss=.6)
emissive = bsk.Material()

# Add Nodes
node = bsk.Node(mesh=monkey_mesh, material=emissive, rotation=(0, 3.14, 0))
scene.add(node)

# Kuwahara tools
kuwahara_shader = bsk.Shader(engine, 'shader/frame.vert', 'shader/kuwahara.frag')
kuwahara_renderer = bsk.Framebuffer(engine, kuwahara_shader)
kuwahara_fbo = bsk.Framebuffer(engine)

while engine.running:
    scene.update()

    kuwahara_renderer.bind(scene.frame.output_buffer.texture, 'screenTexture', 0)
    kuwahara_renderer.render(kuwahara_fbo, auto_bind=False)
    kuwahara_fbo.render()

    engine.update(render=False)