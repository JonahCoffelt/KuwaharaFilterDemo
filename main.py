import basilisk as bsk

engine = bsk.Engine()
scene = bsk.Scene(engine)

# Load meshes
sphere_mesh = bsk.Mesh('models/sphere.obj')

# Load images
floor_albedo = bsk.Image('textures/floor_albedo.png')
floor_normal = bsk.Image('textures/floor_normal.png')

# Load materials
floor = bsk.Material(texture=floor_albedo, normal=floor_normal, roughness=.2, specular=2, clearcoat=1)
mtl = bsk.Material(emissive_color=(3 * 255, 150, 150))

# Add Nodes
sphere = bsk.Node(mesh=sphere_mesh, material=floor)
scene.add(sphere)

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