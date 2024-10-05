import Presenter.presenter
import Model.model
import View.view

Presenter.presenter.AlbumPresenter(
    Model.model.GetDemoAlbums(),
    View.view.AlbumWindow())
