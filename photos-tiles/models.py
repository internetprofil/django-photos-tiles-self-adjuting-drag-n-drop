from django.db import models
from django.utils.translation import ugettext_lazy as _

from adminsortable.models import Sortable
from adminsortable.fields import SortableForeignKey
from tinymce.models import HTMLField
    
class Story(Sortable):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    nameHer = models.CharField(max_length=255, blank=True)
    nameHis = models.CharField(max_length=255, blank=True)
    place = models.CharField(max_length=255)

    leftText = HTMLField(_('Left text'))
    rightText = HTMLField(_('Right text'))
    bottomText = HTMLField(_('Bottom text'))

    teaserPicture = models.ImageField(_('Teaser Picture'),upload_to='weddings')

    class Meta(Sortable.Meta):
        verbose_name = _('Story')
        verbose_name_plural = _('Stories')
    
    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = self.slug.lower()
        super(Story, self).save(*args, **kwargs)

class PhotosStory(Sortable):
    story = SortableForeignKey(Story, related_name='slides',
                                 verbose_name=_('Gallery'))

    published = models.BooleanField(_('Published'), default=True)

    imageField1 = models.ImageField(_('Image'),upload_to='weddings',blank=True)
    imageField2 = models.ImageField(_('Image'),upload_to='weddings',blank=True)
    imageField3 = models.ImageField(_('Image'),upload_to='weddings',blank=True)

    template = models.CharField(max_length=255,choices = (('1','one photo'),
                                           ('2','two photo'),
                                           ('3','three photo')
                                ))

    class Meta(Sortable.Meta):
        verbose_name = _('Photo')
        verbose_name_plural = _('Photos')
        
    def __unicode__(self):
        return self.story.title
