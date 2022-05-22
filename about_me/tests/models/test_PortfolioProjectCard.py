import pytest

from about_me.models import PortfolioProjectCard
import tempfile


@pytest.mark.django_db
def test_ProjectCard_create():
    project_card = PortfolioProjectCard.objects.create(
        name='name',
        logo_img=tempfile.NamedTemporaryFile(suffix=".jpg").name,
        cover_img=tempfile.NamedTemporaryFile(suffix=".jpg").name,
        project_type='project',
        web_version_link=None,
        description='description',
        sort_index=5,
        slowly_redirect=False,
    )
    assert project_card.name == 'name'
    # assert project_card.logo_img == tempfile.NamedTemporaryFile(suffix=".jpg").name
    # assert project_card.cover_img == tempfile.NamedTemporaryFile(suffix=".jpg").name
    assert project_card.project_type == 'project'
    assert project_card.web_version_link is None
    assert project_card.description == 'description'
    assert project_card.sort_index == 5
    assert project_card.slowly_redirect is False
