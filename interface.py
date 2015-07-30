# extract the first word, and call it "operator"

#Is the operator "from"
	#do we have a stored destination?
		#google using the rest of the message and the stored destination
	# else:
		# save the rest of the message as the origin
		# Request the destination
#ok, how about "to"
	# do we have a stored origin
		# google using the stored origin and the rest of the message
	# else:
		# save the rest of the message as the destination
		# Request the origin
# so we don't know the operator.
# Do we have a saved origin?
	# then this must be the destination
	# google using the saved origin and the rest of the message
# we dont have a saved origin, so this must be it
	# save the message as the origin
	# prompt for the destination
