# from napari_tabu import threshold, image_arithmetic

# add your tests here...


def test_something(make_napari_viewer):
    viewer = make_napari_viewer()

    import numpy as np
    layer = viewer.add_image(np.random.random((10,10)))

    from napari_tabu._function import send_selected_to_new_window, open_in_new_window
    send_selected_to_new_window(viewer)

    open_in_new_window(layer, viewer)
